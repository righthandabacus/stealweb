#!/usr/bin/env python
import logging
import re
import argparse
import codecs
import os
import urlparse
import urllib

from lxml import etree, objectify
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

def samedomain(domain1, domain2):
    "Given two host names, tell if they are in the same domain"
    assert(isinstance(domain1,basestring) and isinstance(domain2,basestring))
    part1 = reversed(filter(None,domain1.lower().split('.')))
    part2 = reversed(filter(None,domain2.lower().split('.')))
    assert(part1 and part2)
    return all(a==b for a,b in zip(part1, part2))

###################################
# Content XPath extractor factory
#
def css_select_factory(css):
    'Return function to get elements from tree root based on a CSS selector'
    return lambda domtree: domtree.getroot().cssselect(css)

def xpath_select_factory(xpath):
    'Return function to get elements from tree root based on a XPath selector'
    return lambda domtree: domtree.getroot().xpath(xpath)

def selector_chainer(selectors):
    '''Return function to get elements from tree root based on a list of
    selectors. First successful selection returns'''
    assert(all(callable(x) for x in selectors))
    def __selector(domtree):
        for fn in selectors:
            selection = fn(domtree)
            if selection:
                return selection
    return __selector

def set_checker_factory(strset):
    'Return function to check if input set of string overlap with anything in the predefined set'
    if isinstance(strset,basestring):
        strset = filter(None,strset.split())
    assert(isinstance(strset,(list,tuple,frozenset,set)) and all(isinstance(x,basestring) for x in strset))
    if not isinstance(strset,frozenset):
        strset = frozenset(strset)
    return lambda c: c & strset

def bad_tag_checker(badtags):
    'Return checker fuction: tell if an element is any of the predefined tags'
    checker = set_checker_factory(badtags)
    return lambda elem: bool(checker(set(elem.tag)))

get_elem_class = lambda elem: set(filter(None, (elem.get('class') or '').split()))

def bad_class_checker(badclasses):
    'Return checker fuction: tell if an element is in any of the predefined classes'
    checker = set_checker_factory(badclasses)
    return lambda elem: bool(checker(get_elem_class(elem)))

def checker_chainer(checkers):
    'Return function to tell if an element is hit by any of the provided checkers'
    assert(all(callable(x) for x in checkers))
    return lambda elem: any(x(elem) for x in checkers)

def identifier_factory(selector, checker):
    'Return a function that takes a lxml ElementTree and return XPaths of all content-bearing elements'
    if isinstance(selector, (list,tuple)):
        selector = selector_chainer(selector)
    if isinstance(checker, (list,tuple)):
        checker = checker_chainer(checker)
    assert(callable(selector) and callable(checker))
    # real function
    def _identifier(domtree):
        xpaths = set([])
        badxpaths = set([])
        parent_elems = selector(domtree)
        for e in parent_elems:
            xpaths.add(domtree.getpath(e))
            for x in e.iterdescendants():
                this_xpath = domtree.getpath(x)
                if any(this_xpath.startswith(p) for p in badxpaths):
                    continue # inside known ignorable elements
                if checker(x):
                    if not this_xpath.endswith('/'):
                        this_xpath += '/'
                    badxpaths.add(this_xpath) # decided to skip this
                else:
                    xpaths.add(this_xpath) # this descendent element is good
        logging.info('%d content elements found' % len(xpaths))
        return xpaths
    return _identifier


###################################
# Site-specific items
#
def get_content_xpaths(browser, domtree=None):
    "diverter: return set of xpaths string that identifies as main content"
    url = browser.current_url
    host = gethost(url)
    if samedomain(host,'medium.com') or host.startswith('medium.'):
        return medium_com(domtree)
    if samedomain(host,'cliffsnotes.com'):
        return cliffsnotes_com(domtree)
    if any(samedomain(host,x) for x in ['wordpress.com','pentoy.hk']):
        return wordpress_com(domtree)
    if samedomain(host, 'localpresshk.com'):
        return localpresshk_com(domtree)
    if samedomain(host, 'theinitium.com'):
        return theinitium_com(domtree)
    if host == 'blog.mailgun.com':
        return blog_mailgun_com(domtree)
    if host.split('.')[-2] == 'blogspot' or samedomain(host,'commentshk.com'):
        return blogspot_com(domtree)
    if host == 'opinion.udn.com':
        return opinion_udn_com(domtree)
    if host == 'hk.apple.nextmedia.com':
        return hk_apple_nextmedia_com(domtree)
    if host == 'commondatastorage.googleapis.com' and 'commondatastorage.googleapis.com/letscorp_archive/archives' in url:
        return wordpress_com(domtree) # same as wordpress although it's not
    if host == 'qz.com':
        return qz_com(domtree)
    if host == 'jcjc-dev.com' or host == 'research.googleblog.com':
        return jcjcdev_com(domtree)
    if samedomain(host,'thestandnews.com'):
        return thestandnews_com(domtree)
    if samedomain(host,'analyticsvidhya.com'):
        return analyticsvidhya_com(domtree)
    if samedomain(host,'epochtimes.com'):
        return epochtimes_com(domtree)
    if samedomain(host,'hk01.com'):
        return hk01_com(domtree)
    if samedomain(host,'letscorp.net'):
        return letscorp_net(domtree)
    if samedomain(host,'passiontimes.hk'):
        return passiontimes_hk(domtree)
    if samedomain(host,'rfa.org'):
        return rfa_org(domtree)
    if samedomain(host,'thn21.com'):
        return thn21_com(domtree)
    if samedomain(host,'vjmedia.com.hk'):
        return vjmedia_com_hk(domtree)
    if samedomain(host,'nytimes.com'):
        return nytimes_com(domtree)
    if samedomain(host,'scmp.com'):
        return scmp_com(domtree)
    raise NotImplemented # all other are not known

common_bad_tags = bad_tag_checker("style script meta ins aside")
common_bad_classes = bad_class_checker("social-wrapper ad-wrapper share-wrap share-links sharedaddy "
                        "post-sidebar post-comments comments related-content")
facebook_classes = lambda elem: any(c.startswith('fb_') or c.startswith('fb-') or c in ['float_bar','fsb-social-bar']
                                    for c in get_elem_class(elem))
wordpress_classes = bad_class_checker("wpa wpcnt gp-widget gp-comments gp-related-posts")

medium_com = identifier_factory(
        css_select_factory("main .section-content .section-inner")
       ,common_bad_tags)

opinion_udn_com = identifier_factory(
        css_select_factory("main")
       ,[common_bad_tags, facebook_classes])

hk_apple_nextmedia_com = identifier_factory(
        css_select_factory(".LHSContent h1 , .LHSContent .Article")
       ,[common_bad_tags, bad_tag_checker('fb:like')])

cliffsnotes_com = identifier_factory(
        xpath_select_factory("//article//h2 | //article//*[@class='litNoteText']")
       ,common_bad_tags)

jcjcdev_com = identifier_factory(
        css_select_factory(".post")
       ,[common_bad_tags, common_bad_classes])

qz_com = identifier_factory(
        css_select_factory('article.item *[itemprop~="headline"] , article.item *[itemprop~="image"], article.item *[itemprop~=""] , article.item .featured-image-caption ,  article.item .byline , article.item .item-timestamp , article.item .item-body')
       ,[common_bad_tags, bad_class_checker("item-share-tools article-aside")])

blog_mailgun_com = identifier_factory(
        css_select_factory(".post-title , .byline , .post-body")
       ,[common_bad_tags, common_bad_classes])

blogspot_com = identifier_factory(
        [css_select_factory(".hentry .entry-title , .entry-content")
        ,css_select_factory(".hentry .post-title , .post-body")]
       ,[common_bad_tags, bad_class_checker("similiar blog-pager")])

localpresshk_com = identifier_factory(
        css_select_factory(".gp-single .entry-header .entry-title , .gp-single .entry-header .entry-meta , .entry-content")
       ,[common_bad_tags, common_bad_classes, wordpress_classes])

wordpress_com = identifier_factory(
        [css_select_factory(".entry-title , .entry-meta , .entry-content")
        ,css_select_factory(".posttitle , .postmeta , .postentry")
        ,css_select_factory(".post-title , .post-meta , .post-content")
        ,css_select_factory(".post h2 , .post .info , .post .content , .post .meta , .post .main")
        ,css_select_factory(".itemhead , .itemtext")]
       ,[common_bad_tags, common_bad_classes, wordpress_classes])

theinitium_com = identifier_factory(
        css_select_factory(".article-body h1 , .article-content")
       ,[common_bad_tags, common_bad_classes])

thestandnews_com = identifier_factory(
        css_select_factory(".article-content-wrap .article-name , .article-content-wrap .date , .article-media , .article-content-wrap .caption , .article-content")
       ,[common_bad_tags,
         bad_class_checker("article-ad mobile-ad social-wrap hidden-print article-nav artile-comments-heading article-comments")])

analyticsvidhya_com = identifier_factory(
        css_select_factory("article.main-content .entry-title , article .text-content")
       ,[common_bad_tags, common_bad_classes, bad_class_checker('jp-relatedposts')])

epochtimes_com = identifier_factory(
        css_select_factory(".arttop , #artbody")
       ,[common_bad_tags, bad_class_checker('articleBodyTopBar related-list related-news article_bottom')])

hk01_com = identifier_factory(
        css_select_factory(".article__body__header , .article__body__content")
       ,[common_bad_tags, bad_class_checker("nocontent tag_txt add_tag login")])

letscorp_net = identifier_factory(
        css_select_factory(".post h1 , .post info , .post .content")
       ,[common_bad_tags, bad_class_checker("font-resizer addcomment comments")])

passiontimes_hk = identifier_factory(
        css_select_factory(".article-body , article h1 , article h2 , article h3 article h4 , article h5 , article h6")
       ,[common_bad_tags, common_bad_classes])

rfa_org = identifier_factory(
        css_select_factory("#storycontent h1 , #headerimg , #storytext")
       ,common_bad_tags)

thn21_com = identifier_factory(css_select_factory("#V , .ti"), common_bad_tags)

nytimes_com = identifier_factory(
        css_select_factory("#story #story-meta , #story .story-content")
       ,[bad_class_checker("nocontent sharetools comments-button")])

scmp_com = identifier_factory(
        css_select_factory("main .v2-processed , main #page-title , main .field-items , main .node-published , main .node-updated")
       ,[])

def vjmedia_upto_author(elem):
    for x in elem.getparent().iterchildren():
        if x == elem:
            return False
        elif x.get('id') == 'author-spotlight':
            break
    return True

vjmedia_com_hk = identifier_factory(css_select_factory(".hentry"),vjmedia_upto_author)

###################################
# Main modules
#

def collect_features(browser, debugfile=None):
    '''
    From the current page loaded by the browser, extract page features
    TODO all webdriver calls are damn slow, lxml would be much faster
    '''
    all_elems = browser.get_everything()
    winwidth = browser.get_window_size()['width']
    logging.info("%d web elements found" % len(all_elems))
    page_source = next((x[-1] for x in all_elems if x[1]=='/html/body'),'')
    assert(page_source) # there must be a body, right?
    domtree = html2dom(page_source) # need to pretty format source before use
    objectify.deannotate(domtree, cleanup_namespaces=True)
    linecount = len(page_source.split("\n"))
    if debugfile:
        open(debugfile,'w').write(etree.tostring(domtree, encoding='utf8', pretty_print=True, method='xml'))

    # populate DOM tree geometry data
    xpathHash = {attrs[1]:i for i,attrs in enumerate(all_elems)}
    depthHash = {} # actually "height", distance from node to deepest leaf
    def findElementDepth(e):
        if e not in depthHash:
            if len(e):
                depthHash[e] = 1 + max(findElementDepth(x) for x in e.iterchildren())
            else:
                depthHash[e] = 0
        return depthHash[e]

    # collect element attributes:
    attributes = []
    try:
        content_xpaths = get_content_xpaths(browser, domtree)
    except NotImplemented:
        logging.critical('No content identifier for URL %s' % browser.current_url)
        content_xpaths = []
    for i,attrs in enumerate(all_elems):
        if i and (i % 1000 == 0):
            logging.info('...on element #%d' % i)
        elem, xpath, visible, x, y, wid, hght, fgcolor, bgcolor, textonly, htmlcode = attrs
        if not xpath or re.search(r'[^a-z0-9\[\]\/]',xpath) or re.search(r'(?<!\w)(script|head)(?!\w)',xpath):
            continue # skip these to avoid pollution by JS or HTML header
        etreenode  = domtree.xpath(xpath)
        if len(etreenode) != 1:
            if not etreenode:
                logging.error('WebDriver reported XPath cannot be found in lxml: %s' % xpath)
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
        textxws = sum(1 for c in textonly if c and not c.isspace()) # text length excluding whitespaces
        if not htmllen:
            logging.error('empty HTML for tag %s on line %s at (%s,%s)+(%s,%s)' % (tagname, sourceline, x,y,wid,hght))
        textclip   = abbreviate(textonly)
        sourcepct  = float(sourceline)/linecount
        xpct       = float(x)/winwidth
        pospct     = float(i+1)/len(all_elems)
        isgood     = 1 if visible and xpath in content_xpaths else 0
        # remember this
        attributes.append([i, parent, tagname, depth, childcount, sourceline, sourcepct, pospct, xpct, x, y,
            wid, hght, fgcolor, bgcolor, textxws, textlen, htmllen, visible, xpath, textclip, isgood])

    header = ("id parent tagname depth childcount sourceline sourcepct pospct xpct x y "
        "wid hght fgcolor bgcolor textxws textlen htmllen visible xpath textclip goodness").split()
    return header, attributes

def parseargs():
    parser = argparse.ArgumentParser(
                description='Webpage crawler and feature analyser'
               ,formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("url", help="starting URL to crawl, example: https://www.cliffsnotes.com/literature/p/the-prince/book-summary")
    parser.add_argument("-d", dest="dir", default='training_data', help="directory to store pages")
    parser.add_argument("-x", dest="debug", action="store_true", default=False, help="debug: to save lxml parsed version of the web page as well")
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
    if args.debug:
        debgufile = os.path.join(args.dir, html)+'.lxml'
    else:
        debugfile = None
    header, attributes = collect_features(browser, debugfile)
    logging.info('%d elements reported' % len(attributes))
    # write as CSV
    with open(os.path.join(args.dir, csv), 'wb') as csvfile:
        csvfile.write(codecs.BOM_UTF8) # Excel requires BOM
        csvout = UnicodeWriter(csvfile)
        csvout.writerow(header)
        csvout.writerows([[x if isinstance(x,basestring) else str(x) for x in row] for row in attributes])
    logging.info('Wrote to %s' % csv)

if __name__ == '__main__':
    from debugger import debugExceptions
    debugExceptions()
    logging.basicConfig(level=logging.INFO  # level DEBUG will be noisy with selenium
                       ,format='%(asctime)-15s %(levelname)s:%(name)s:%(message)s')
    main()

# vim:set nowrap et ts=4 sw=4:
