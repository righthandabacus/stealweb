#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Crawl web pages and save visual features into CSV

Web page are crawled by CEF, and visual features are extracted by Javascript
executed under CEF.
'''

from __future__ import division
import argparse
import codecs
import logging
import os
import re
import time
import threading

from fakechrome import fakechrome, cef
from lxml import etree, objectify
from utf8csv import UnicodeWriter
from utils import configLogger, escape_url, condense_space, abbreviate, html2dom, \
                  gethost, samedomain, str2unicode, any2unicode

logger = logging.getLogger('crawler')

def url2filenames(url):
    assert(url.startswith('http://') or url.startswith('https://'))
    filebase = ' '.join(url.replace('/',' ').split()[1:])
    return filebase

###################################
# Main modules
#

def collect_features(browser):
    '''
    Read DOM attributes from the current page loaded by the browser, derive page features

    Args:
        browser (cef): Browser object that with the page already loaded and ready

    Returns:
        tuple (header, attributes, dom, body html): the header and attributes
        are list of attributes which together forms a feature table; dom is the
        raw attributes extracted by JS code, in form of list of lists; the body
        html is the rendered html code of the <body> part of the page

    Data dictionary of collect_features() output:
      id          [int] seq num of node in JS dom tree
      parent      [int] id of parent node
      tagname     [str] HTML tag name
      depth       [int] node count to its deepest descendent in dom tree (etree-based)
      childcount  [int] num of children
      sourceline  [int] line num of source code (etree-based, i.e. start from <body> tag)
      sourcepct   [float] percentage position of source line in HTML (etree-based, within <body>)
      pospct      [float] percentage postiion of node in the DOM (depth-first search of JS DOM)
      xpct        [float] percentage position of element's left edge to window width
      x           [int] pixel coordinate of left edge of element's bounding box to the page
      y           [int] pixel coordinate of top edge of element's bounding box to the page
      width       [int] pixel width of element's bounding box
      height      [int] pixel height of element's bounding box
      fgcolor     [str] foreground color, in form of rgb(255,255,255) or rgba(255,255,255,1.0)
      bgcolor     [str] background color, in form of rgb(255,255,255) or rgba(255,255,255,1.0)
      textxws     [int] character length of text excluding whitespaces
      textlen     [int] character length of text
      htmllen     [int] character length of HTML code
      visible     [bool] visibility of this element
      fontsize    [float] font size
      xpath       [str] xpath of element
      textclip    [str] starting and ending snippet of text
    '''
    dom = [[str2unicode(x) for x in row]
           for row in browser.getDOMdata(True)] # synchronous get, and make all string into unicode
    winparam = browser.windowParams
    winwidth = winparam['innerWidth']
    logger.debug("%d web elements found" % len(dom))
    bodyhtml = next((x[-1] for x in dom if x[0]=='/html/body'),'')
    assert(bodyhtml) # we assumed there must be a body
    domtree = html2dom(bodyhtml) # need to pretty format source before use
    objectify.deannotate(domtree, cleanup_namespaces=True)
    linecount = len(bodyhtml.split("\n"))

    # populate DOM tree geometry data
    xpathHash = {attrs[0]:i for i,attrs in enumerate(dom)}
    depthHash = {} # actually "height", distance from node to deepest leaf, based on lxml etree
    def findElementDepth(e):
        "e: lxml etree element node, find its depth in dom tree"
        if e not in depthHash:
            if len(e): # e has children
                depthHash[e] = 1 + max(findElementDepth(x) for x in e.iterchildren())
            else: # e has no children, by definition depth=0
                depthHash[e] = 0
        return depthHash[e]

    # collect element attributes:
    attributes = []
    for i,attrs in enumerate(dom):
        if i and (i % 1000 == 0):
            logger.debug('...on element #%d' % i)
        xpath, display, visible, x, y, width, height, fgcolor, bgcolor, fontsize, textonly, htmlcode = attrs
        if not xpath or re.search(r'[^a-z0-9\[\]\/]',xpath) or re.search(r'(?<!\w)(script|head)(?!\w)',xpath):
            continue # skip these to avoid pollution by JS or HTML header
        etreenode  = domtree.xpath(xpath)
        if len(etreenode) != 1:
            if not etreenode:
                logger.error('JS reported XPath cannot be found in lxml: %s' % xpath)
                continue
            else:
                logger.error('XPath not unique for %s. %d elements found.' % (xpath, len(etreenode)))
        parent     = xpathHash.get(xpath.rsplit('/',1)[0])
        tagname    = xpath.rsplit('/',1)[-1].split('[',1)[0]
        depth      = findElementDepth(etreenode[0])
        if etreenode:
            childcount = len(etreenode)
        else:
            childcount = len(n for n in xpathHash if n.startwith(xpath) and '/' not in n[len(xpath):])
        sourceline = etreenode[0].sourceline
        fgcolor    = fgcolor.replace(' ','')
        bgcolor    = bgcolor.replace(' ','')
        textonly   = condense_space(textonly) # text from JS retains word boundary by replacing tag with space while etree.tostring() just remove tags
        htmlcode   = condense_space(htmlcode)
        if not htmlcode: # JS cannot give out the HTML, use etree version instead
            htmlcode = condense_space(etree.tostring(etreenode[0], encoding='utf8', method='html').decode('utf8'))
        # derived data
        textlen, htmllen = len(textonly), len(htmlcode)
        textxws = sum(1 for c in textonly if c and not c.isspace()) # text length excluding whitespaces
        if not htmllen:
            logger.error('empty HTML for tag %s on line %s at (%s,%s)+(%s,%s)' % (tagname, sourceline, x,y,width,height))
        textclip   = abbreviate(textonly)
        sourcepct  = sourceline/linecount
        xpct       = x/winwidth
        pospct     = (i+1)/len(dom)
        # remember this
        attributes.append([i, parent, tagname, depth, childcount, sourceline, sourcepct, pospct, xpct, x, y,
            width, height, fgcolor, bgcolor, textxws, textlen, htmllen, min(visible,display), fontsize,
            xpath, textclip])

    header = ("id parent tagname depth childcount sourceline sourcepct pospct xpct x y width height "
              "fgcolor bgcolor textxws textlen htmllen visible fontsize xpath textclip").split()
    return header, attributes, dom, bodyhtml

###################################
# main program
#

def parseargs():
    parser = argparse.ArgumentParser(description='Crawl webpage(s) and analyse for DOM features'
                                    ,formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("url", help="URL to crawl or text file containing URLs in lines")
    parser.add_argument("-d", dest="dir", default='training_data', help="directory to store pages")
    parser.add_argument("-s", dest="sleep", default=0, type=int, help="delay between page load and processing")

    parser.add_argument("-x", dest="debug", action="store_true", default=False, help="debug: to save lxml parsed version of the web page as well")

    parser.add_argument("-v", dest="verbose", action='store_true', default=False, help="show verbose debug message")
    parser.add_argument("-q", dest="quiet", action='store_true', default=False, help="show no message")
    return parser.parse_args()

def crawl_url(browser, url , savedir, debug=False, delay=0):
    html = url2filenames(url)
    browser.LoadUrl(escape_url(url), synchronous=True)
    logger.info('Fetched '+url)
    if delay:
        time.sleep(delay)
    # save raw page
    htmlfile = os.path.join(savedir, html)
    with open(htmlfile, 'wb') as srcfp:
        html = browser.getSource(True) # synchronous get
        assert(html)
        srcfp.write(html)
        logger.debug('Wrote to %s' % htmlfile)
    # parse page for features, get attribute table
    logger.info('Extracting features')
    header, attributes, dom, bodyhtml = collect_features(browser)
    logger.debug('%d elements with features extracted' % len(attributes))
    # write as CSV
    csvfile = htmlfile + '.csv'
    with open(csvfile, 'wb') as csvfp:
        csvfp.write(codecs.BOM_UTF8) # Excel requires BOM
        csvout = UnicodeWriter(csvfp)
        csvout.writerow(header)
        csvout.writerows([[any2unicode(x) for x in row] for row in attributes])
    logger.info('Wrote to %s' % csvfile)
    if debug:
        lxmlfile = htmlfile+'.lxml'
        domfile = htmlfile+'.raw.csv'
        with open(domfile, 'wb') as csvfp: # write DOM csv as recognized by JS
            csvfp.write(codecs.BOM_UTF8) # Excel requires BOM
            csvout = UnicodeWriter(csvfp)
            csvout.writerow(
                "xpath display visible x y width height fgcolor bgcolor fontsize "
                "textonly htmlcode".split()
            )
            csvout.writerows([[any2unicode(x) for x in row] for row in dom])
        logger.info('Wrote to %s' % domfile)
        with open(lxmlfile, 'wb') as fp:
            fp.write(bodyhtml.encode('utf8'))
        logger.info('Wrote to %s' % lxmlfile)

def crawlmain(browser, args):
    if os.path.exists(args.url):
        with open(args.url, 'r') as urlfp:
            for url in urlfp:
                crawl_url(browser, url.strip(), args.dir, args.debug, args.sleep)
    else:
        crawl_url(browser, args.url, args.dir, args.debug, args.sleep)
    # close browser, signal MessageLoop to stop
    browser.CloseBrowser()

def main():
    from utils import configLogger
    args = parseargs()
    configLogger(quiet=args.quiet, debug=args.verbose)
    browser = fakechrome(headless=True).getBrowser()
    logger.debug('Browser loaded')
    workthread = threading.Thread(target=crawlmain, args=(browser, args))
    workthread.start()
    logger.debug('Running CEF message loop')
    cef.MessageLoop() # blocking until browser closed
    logger.debug('Message loop end')
    workthread.join()
    cef.Shutdown()

if __name__ == '__main__':
    main()

# vim:set nowrap et ts=4 sw=4:
