import logging
import re
import argparse
import codecs
import os
import urlparse
import urllib

from lxml import etree
from utf8csv import csv,UnicodeWriter
from phantomjs import phantomjs
import selenium.common.exceptions

###################################
# Helper functions
#

def escape_url(url):
    urlparts = list(urlparse.urlparse(url))
    for i in [2,3,4]:
        if urlparts[i]:
            urlparts[i] = urllib.quote(urlparts[i])
    return urlparse.urlunparse(urlparts)

def condense_space(string):
    if not isinstance(string,basestring):
        if string is not None:
            logging.critical('condense_space return empty string for %r' % string)
        return ''
    return re.sub(r'\s+', ' ', string).strip()

def abbreviate(string, head=20, tail=10):
    if len(string) <= (head+3+tail):
        return string
    return string[:head] + '...' + string[-tail:]

def parse_rgba(rgba):
    assert(rgba.startswith('rgba(') or rgba.startswith('rgb('))
    assert(rgba.endswith(')'))
    if rgba.startswith('rgba('):
        return [float(x) for x in rgba[5:-1].split(",")]
    else:
        return [float(x) for x in rgba[4:-1].split(",")]

def rgba2rgb(rgba):
    '''
    assume a rgba value put on top of white background, find the resulting rgb value
    ref: https://en.wikipedia.org/wiki/Alpha_compositing
    '''
    if len(rgba) == 3: return rgba # pass-thou if no alpha channel
    white = [255, 255, 255]
    rgb = rgba[:3]
    alpha = rgba[3]
    return [alpha*fg+(1.0-alpha)*bg for fg,bg in zip(rgb,white)]

def luminance(rgb):
    '''
    find luminance from rgba color using BT.709 standard, formula: Y = (0.2126R+0.7152G+0.0722B)*alpha
    assume all elements are put on top of white background
    ref: https://en.wikipedia.org/wiki/YUV
    '''
    Y = 0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]
    return Y

def html2dom(htmlstr):
    parser = etree.HTMLParser(remove_blank_text=True, remove_comments=True, remove_pis=True)
    domtree = etree.fromstring(htmlstr, parser)
    return etree.ElementTree(domtree)

def url2filenames(url):
    assert(url.startswith('http://') or url.startswith('https://'))
    filebase = ' '.join(url.replace('/',' ').split()[1:])
    return filebase, filebase+'.csv'

gethost = lambda url: urlparse.urlparse(url).netloc


###################################
# Site-specific items
#
def get_content_xpaths(browser, domtree=None):
    "diverter: return set of xpaths string that identifies as main content"
    url = browser.current_url
    host = gethost(url)
    if host.endswith('medium.com'):
        return medium_com(browser, domtree)
    if host.endswith('cliffsnotes.com'):
        return cliffsnotes_com(browser, domtree)
    if host.endswith('wordpress.com'):
        return wordpress_com(browser, domtree)
    if host.endswith('theinitium.com'):
        return theinitium_com(browser, domtree)
    if host.split('.')[-2] == 'blogspot' or host.endswith('commentshk.com'):
        return blogspot_com(browser, domtree)
    if host == 'opinion.udn.com':
        return opinion_udn_com(browser, domtree)
    raise NotImplemented # all other are not known

def medium_com(browser, domtree=None):
    '''
    Article on medium.com, this extract all WebElements that identifies main
    content and return their XPath
    '''
    main_elems = browser.find_elements_by_css_selector("main .section-content .section-inner")
    logging.info('%d container element found on medium.com' % len(main_elems))
    xpaths = set([])
    for e in main_elems:
        xpaths.add(browser.get_xpath(e))
        for x in e.find_elements_by_xpath("*|*//*"):
            xpaths.add(browser.get_xpath(x))
    logging.info('%d total elements found on medium.com' % len(xpaths))
    return xpaths

def opinion_udn_com(browser, domtree=None):
    "Article on opinion.udn.com"
    main_elems = browser.find_elements_by_css_selector("main")
    xpaths = set([])
    for e in main_elems:
        for x in e.find_elements_by_xpath("*|*//*"):
            if x.tag_name == 'script':
                continue # skip tag: script
            classes = (x.get_attribute('class') or "").split()
            if any(c.startswith('fb_') or c.startswith('fb-') or c=='float_bar' for c in classes):
                continue # skip class: fb_* fb-* float_bar
            xpaths.add(browser.get_xpath(x))
    logging.info('%d total elements found on opinion.udn.com' % len(xpaths))
    return xpaths

def cliffsnotes_com(browser, domtree=None):
    "Article on cliffsnotes.com"
    xpaths = set([])
    if domtree:
        main_elems = domtree.xpath("//article[.//p[@class='litNoteText']]")
        for e in main_elems:
            for x in e.iterchildren():
                classes = (x.get('class') or "").split()
                if x.tag not in "h1 h2 h3 h4 h5 h6".split() and 'litNoteText' not in classes:
                    continue # these are surely not main text
                xpaths.add(domtree.getpath(x))
                for y in x.iterchildren():
                    xpaths.add(domtree.getpath(y))
    else:
        main_elems = browser.find_elements_by_xpath("//article[.//p[@class='litNoteText']]")
        for e in main_elems:
            for x in e.find_elements_by_xpath("*"):
                classes = (x.get_attribute('class') or "").split()
                if x.tag_name not in "h1 h2 h3 h4 h5 h6".split() and 'litNoteText' not in classes:
                    continue # these are surely not main text
                xpaths.add(browser.get_xpath(x))
                for y in x.find_elements_by_xpath("*|*//*"):
                    xpaths.add(browser.get_xpath(y))
    logging.info('%d total elements found on cliffsnotes.com' % len(xpaths))
    return xpaths

def blogspot_com(browser, domtree=None):
    xpaths = set([])
    badxpaths = set([])
    main_elems = domtree.getroot().cssselect(".hentry .entry-title , .entry-content")
    if not len(main_elems):
        main_elems = domtree.getroot().cssselect(".hentry .post-title , .post-body")
    for e in main_elems:
        xpaths.add(domtree.getpath(e))
        for x in e.iterdescendants():
            this_xpath = domtree.getpath(x)
            if any(this_xpath.startswith(p) for p in badxpaths):
                continue # inside known ignorable elements
            if x.tag in "style script meta".split():
                badxpaths.add(domtree.getpath(x))
                continue # these are surely not main text
            xpaths.add(domtree.getpath(x))
    logging.info('%d total elements found on blogspot.com' % len(xpaths))
    return xpaths

def wordpress_com(browser, domtree=None):
    xpaths = set([])
    badxpaths = set([])
    main_elems = domtree.getroot().cssselect(".entry-title , .entry-meta , .entry-content")
    if not len(main_elems):
        main_elems = domtree.getroot().cssselect(".itemhead , .itemtext")
    for e in main_elems:
        xpaths.add(domtree.getpath(e))
        for x in e.iterdescendants():
            classes = set(filter(None,(x.get('class') or "").split()))
            this_xpath = domtree.getpath(x)
            if any(this_xpath.startswith(p) for p in badxpaths):
                continue # inside known ignorable elements
            if x.tag in "style script meta".split() or (set("wpa wpcnt sharedaddy comments".split()) & classes):
                badxpaths.add(domtree.getpath(x))
                continue # these are surely not main text
            xpaths.add(domtree.getpath(x))
    logging.info('%d total elements found on wordpress.com' % len(xpaths))
    return xpaths

def theinitium_com(browser, domtree=None):
    xpaths = set([])
    badxpaths = set([])
    main_elems = domtree.getroot().cssselect(".article-body h1 , .article-content")
    for e in main_elems:
        xpaths.add(domtree.getpath(e))
        for x in e.iterdescendants():
            classes = set(filter(None,(x.get('class') or "").split()))
            this_xpath = domtree.getpath(x)
            if any(this_xpath.startswith(p) for p in badxpaths):
                continue # inside known ignorable elements
            if x.tag in "form style script meta".split() or (set("ad-wrapper share-wrap related-content comments".split()) & classes):
                badxpaths.add(domtree.getpath(x))
                continue # these are surely not main text
            xpaths.add(domtree.getpath(x))
    logging.info('%d total elements found on theinitium.com' % len(xpaths))
    return xpaths

###################################
# Main modules
#

def collect_features(browser):
    '''
    From the current page loaded by the browser, extract page features
    TODO all webdriver calls are damn slow, lxml would be much faster
    '''
    all_elems = browser.get_everything()
    page_source = browser.page_source
    domtree = html2dom(page_source) # need to pretty format source before use
    linecount = len(page_source.split("\n"))
    winwidth = browser.get_window_size()['width']
    logging.info("%d web elements found" % len(all_elems))

    # populate DOM tree geometry data
    xpathHash = {attrs[1]:i for i,attrs in enumerate(all_elems)}
    depthHash = {}
    def findElementDepth(e):
        if e not in depthHash:
            if len(e):
                depthHash[e] = 1 + max(findElementDepth(x) for x in e.iterchildren())
            else:
                depthHash[e] = 0
        return depthHash[e]

    # collect element attributes
    attributes = []
    try:
        content_xpaths = get_content_xpaths(browser, domtree)
    except NotImplemented:
        logging.critical('No content identifier for URL %s' % browser.current_url)
        content_xpaths = []
    for i,attrs in enumerate(all_elems):
        if i and (i % 50 == 0):
            logging.info('...on element #%d' % i)
        if len(attrs) != 10:
            print i
            print attrs
        elem, xpath, x, y, wid, hght, fgcolor, bgcolor, textonly, htmlcode = attrs
        if not xpath or re.search(r'(?<!\w)(script|head)(?!\w)',xpath):
            continue # skip these to avoid pollution by JS or HTML header
        etreenode  = domtree.xpath(xpath)
        if len(etreenode) != 1:
            if not etreenode:
                continue
            else:
                logging.error('XPath not unique for %s. %d elements found.' % (xpath, len(etreenode)))
        parent     = xpathHash.get(xpath.rsplit('/',1)[0])
        tagname    = xpath.rsplit('/',1)[-1].split('[',1)[0]
        depth      = findElementDepth(etreenode[0])
        if etreenode:
            childcount = len(etreenode)
        else:
            childcount = len(elem.find_elements_by_xpath("*"))
        sourceline = etreenode[0].sourceline
        fgcolor    = fgcolor.replace(' ','')
        bgcolor    = bgcolor.replace(' ','')
        textonly   = condense_space(textonly) # phantomjs text is better than etree.tostring() for the former will replace tags with space if necessary while latter is simply removing tags
        htmlcode   = condense_space(htmlcode)
        if not htmlcode: # phantomjs cannot give out the HTML, use etree version instead
            htmlcode = condense_space(etree.tostring(etreenode[0], encoding='utf8', method='html').decode('utf8'))
        # derived data
        textlen, htmllen = len(textonly), len(htmlcode)
        if not htmllen:
            logging.error('empty HTML for tag %s on line %s at (%s,%s)+(%s,%s)' % (tagname, sourceline, x,y,wid,hght))
        textratio  = (float(textlen) / htmllen) if htmllen else 'NaN'
        textclip   = abbreviate(textonly)
        sourcepct  = float(sourceline)/linecount
        lumdiff    = luminance(rgba2rgb(parse_rgba(bgcolor))) - luminance(rgba2rgb(parse_rgba(fgcolor)))
        xpct       = float(x)/winwidth
        pospct     = float(i+1)/len(all_elems)
        area       = wid*hght
        #isgood     = 1 if any(xpath.startswith(x) for x in content_xpaths) else 0
        isgood     = 1 if xpath in content_xpaths else 0
        # remember this
        attributes.append([i, parent, tagname, depth, childcount, sourceline, sourcepct, pospct, xpct, x, y,
            wid, hght, area, fgcolor, bgcolor, lumdiff, textlen, htmllen, textratio, xpath, textclip, isgood])

    header = ("id parent tagname depth childcount sourceline sourcepct pospct xpct x y "
        "wid hght area fgcolor bgcolor lumdiff textlen htmllen textratio xpath textclip goodness").split()
    return header, attributes

def parseargs():
    parser = argparse.ArgumentParser(
                description='Webpage crawler and feature analyser'
               ,formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("url", help="starting URL to crawl, example: https://www.cliffsnotes.com/literature/p/the-prince/book-summary")
    parser.add_argument("-d", dest="dir", default='training_data', help="directory to store pages")
    #parser.add_argument("-d", dest="debug", action="store_true", default=False, help="debug: to save crawled pages")
    #parser.add_argument("-o", dest="output", default="output.html", help="output HTML file name")
    return parser.parse_args()

###################################
# main program
#
def main():
    args = parseargs()
    html,csv = url2filenames(args.url)
    # Start PhantomJS, crawl page
    browser = phantomjs()
    logging.info('PhantomJS loaded')
    browser.get(escape_url(args.url))
    logging.info(escape_url(args.url))
    logging.info('Fetched '+args.url)
    # save raw page
    open(os.path.join(args.dir, html), 'wb').write(browser.page_source.encode('utf8'))
    # parse page for features, get attribute table
    logging.info('Extracting features')
    header, attributes = collect_features(browser)
    logging.info('%d elements reported' % len(attributes))
    # write as CSV
    with open(os.path.join(args.dir, csv), 'wb') as csvfile:
        csvfile.write(codecs.BOM_UTF8) # Excel requires BOM
        csvout = UnicodeWriter(csvfile)
        csvout.writerow(header)
        csvout.writerows([[x if isinstance(x,basestring) else str(x) for x in row] for row in attributes])
    logging.info('Wrote to %s' % csv)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO  # level DEBUG will be noisy with selenium
                       ,format='%(asctime)-15s %(levelname)s:%(name)s:%(message)s')
    main()

# vim:set nowrap et ts=4 sw=4:
