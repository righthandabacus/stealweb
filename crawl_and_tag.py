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


###################################
# Site-specific items
#
def xpath_extractor_factory(css_selectors=[], xpath_selectors=[], bad_tags=[], bad_classes=[], is_bad=None):
    # sanity checkers
    assert(isinstance(xpath_selectors,(list,tuple)))
    assert(isinstance(css_selectors,(list,tuple)))
    assert(not xpath_selectors or not css_selectors)
    assert(all(isinstance(x,basestring) for x in css_selectors))
    assert(all(isinstance(x,basestring) for x in xpath_selectors))
    if isinstance(bad_tags, basestring):
        bad_tags = filter(None, bad_tags.split())
    if isinstance(bad_classes, basestring):
        bad_classes = filter(None, bad_classes.split())
    assert(callable(bad_tags) or (isinstance(bad_tags,(list,tuple,set)) and all(isinstance(x,basestring) for x in bad_tags)))
    assert(callable(bad_classes) or (isinstance(bad_classes,(list,tuple,set)) and all(isinstance(x,basestring) for x in bad_classes)))
    if not callable(bad_tags):
        bad_tags = set(bad_tags)
    if not callable(bad_classes):
        bad_classes = set(bad_classes)
    # real function
    def _xpath_extractor(browser, domtree=None):
        xpaths = set([])
        badxpaths = set([])
        for xpath_selector in xpath_selectors:
            main_elems = domtree.getroot().xpath(xpath_selector)
            if len(main_elems): break
        for css_selector in css_selectors:
            main_elems = domtree.getroot().cssselect(css_selector)
            if len(main_elems): break
        for e in main_elems:
            xpaths.add(domtree.getpath(e))
            for x in e.iterdescendants():
                classes = set(filter(None,(x.get('class') or "").split()))
                this_xpath = domtree.getpath(x)
                if any(this_xpath.startswith(p) for p in badxpaths):
                    continue # inside known ignorable elements
                if (bad_tags(x.tag) if callable(bad_tags) else x.tag in bad_tags) or \
                   (bad_classes(classes) if callable(bad_classes) else (classes & bad_classes)) or \
                   (callable(is_bad) and is_bad(x)):
                        badxpaths.add(domtree.getpath(x))
                        continue # these are surely not main text
                xpaths.add(domtree.getpath(x))
        logging.info('%d content elements found' % len(xpaths))
        return xpaths
    return _xpath_extractor

def get_content_xpaths(browser, domtree=None):
    "diverter: return set of xpaths string that identifies as main content"
    url = browser.current_url
    host = gethost(url)
    if host.endswith('.medium.com') or host.startswith('medium.'):
        return medium_com(browser, domtree)
    if host.endswith('.cliffsnotes.com'):
        return cliffsnotes_com(browser, domtree)
    if any(host.endswith(x) for x in ['.wordpress.com','.pentoy.hk']):
        return wordpress_com(browser, domtree)
    if any(host.endswith(x) for x in ['.localpresshk.com']):
        return localpresshk_com(browser, domtree)
    if host.endswith('theinitium.com'):
        return theinitium_com(browser, domtree)
    if host == 'blog.mailgun.com':
        return blog_mailgun_com(browser, domtree)
    if host.split('.')[-2] == 'blogspot' or host.endswith('.commentshk.com'):
        return blogspot_com(browser, domtree)
    if host == 'opinion.udn.com':
        return opinion_udn_com(browser, domtree)
    if host == 'hk.apple.nextmedia.com':
        return hk_apple_nextmedia_com(browser, domtree)
    if host == 'commondatastorage.googleapis.com' and 'commondatastorage.googleapis.com/letscorp_archive/archives' in url:
        return wordpress_com(browser, domtree) # same as wordpress although it's not
    if host == 'qz.com':
        return qz_com(browser, domtree)
    if host == 'jcjc-dev.com' or host == 'research.googleblog.com':
        return jcjcdev_com(browser, domtree)
    if host.endswith('thestandnews.com'):
        return thestandnews_com(browser, domtree)
    if host.endswith('.analyticsvidhya.com'):
        return analyticsvidhya_com(browser, domtree)
    if host.endswith('.epochtimes.com'):
        return epochtimes_com(browser, domtree)
    if host.endswith('.hk01.com'):
        return hk01_com(browser, domtree)
    if host.endswith('.letscorp.net'):
        return letscorp_net(browser, domtree)
    if host.endswith('.passiontimes.hk'):
        return passiontimes_hk(browser, domtree)
    if host.endswith('.rfa.org'):
        return rfa_org(browser, domtree)
    if host.endswith('.thn21.com'):
        return thn21_com(browser, domtree)
    if host.endswith('vjmedia.com.hk'):
        return vjmedia_com_hk(browser, domtree)
    raise NotImplemented # all other are not known

medium_com = xpath_extractor_factory(
        css_selectors=["main .section-content .section-inner"]
        ,bad_tags="style script meta")

opinion_udn_com = xpath_extractor_factory(
        css_selectors=["main"]
        ,bad_tags="style script meta"
        ,bad_classes=lambda classes: any(c.startswith('fb_') or c.startswith('fb-') or c=='float_bar' for c in classes))

hk_apple_nextmedia_com = xpath_extractor_factory(
        css_selectors=[".LHSContent h1 , .LHSContent .Article"]
        ,bad_tags="style script meta fb:like")

cliffsnotes_com = xpath_extractor_factory(
        xpath_selectors=["//article//h2 | //article//*[@class='litNoteText']"]
        ,bad_tags="style script meta")

jcjcdev_com = xpath_extractor_factory(
        css_selectors=[".post"]
        ,bad_tags="style script meta"
        ,bad_classes="social-wrapper share-links post-sidebar post-comments")

qz_com = xpath_extractor_factory(
        css_selectors=['article.item *[itemprop~="headline"] , article.item *[itemprop~="image"], article.item *[itemprop~=""] , article.item .featured-image-caption ,  article.item .byline , article.item .item-timestamp , article.item .item-body']
        ,bad_tags="style script meta"
        ,bad_classes="item-share-tools article-aside")

blog_mailgun_com = xpath_extractor_factory(
        css_selectors=[".post-title , .byline , .post-body"]
        ,bad_tags="style script meta"
        ,bad_classes="share-links post-sidebar post-comments")

blogspot_com = xpath_extractor_factory(
        css_selectors=[".hentry .entry-title , .entry-content"
                      ,".hentry .post-title , .post-body"]
        ,bad_tags="style script meta ins"
        ,bad_classes="similiar blog-pager")

localpresshk_com = xpath_extractor_factory(
        css_selectors=[".gp-single .entry-header .entry-title , .gp-single .entry-header .entry-meta , .entry-content"]
        ,bad_tags="style script meta ins aside"
        ,bad_classes="wpa wpcnt sharedaddy comments gp-widget gp-comments gp-related-posts")

wordpress_com = xpath_extractor_factory(
        css_selectors=[".entry-title , .entry-meta , .entry-content"
                      ,".posttitle , .postmeta , .postentry"
                      ,".post-title , .post-meta , .post-content"
                      ,".itemhead , .itemtext"
                      ,".post h2 , .post .info , .post .content .post h2 , .post .meta , .post .main"]
        ,bad_tags="style script meta ins aside"
        ,bad_classes="wpa wpcnt sharedaddy comments gp-widget gp-comments gp-related-posts fsb-social-bar")

theinitium_com = xpath_extractor_factory(
        css_selectors=[".article-body h1 , .article-content"]
        ,bad_tags="form style script meta"
        ,bad_classes="ad-wrapper share-wrap related-content comments")

thestandnews_com = xpath_extractor_factory(
        css_selectors=[".article-content-wrap .article-name , .article-content-wrap .date , .article-media , .article-content-wrap .caption , .article-content"]
        ,bad_tags="form style script meta"
        ,bad_classes="article-ad mobile-ad social-wrap hidden-print article-nav artile-comments-heading article-comments")

analyticsvidhya_com = xpath_extractor_factory(
        css_selectors=["article.main-content .entry-title , article .text-content"]
        ,bad_tags="style script meta ins"
        ,bad_classes="wpa wpcnt sharedaddy comments jp-relatedposts")

epochtimes_com = xpath_extractor_factory(
        css_selectors=[".arttop , #artbody"]
        ,bad_tags="style script meta ins aside"
        ,bad_classes="articleBodyTopBar related-list related-news article_bottom")

hk01_com = xpath_extractor_factory(
        css_selectors=[".article__body__header , .article__body__content"]
        ,bad_tags="style script meta ins aside"
        ,bad_classes="nocontent tag_txt add_tag login")

letscorp_net = xpath_extractor_factory(
        css_selectors=[".post h1 , .post info , .post .content"]
        ,bad_tags="style script meta ins aside"
        ,bad_classes="font-resizer addcomment comments")

passiontimes_hk = xpath_extractor_factory(
        css_selectors=[".article-body , article h1 , article h2 , article h3 article h4 , article h5 , article h6"]
        ,bad_tags="form style script meta"
        ,bad_classes="ad-wrapper share-wrap related-content comments")

rfa_org = xpath_extractor_factory(
        css_selectors=["#storycontent h1 , #headerimg , #storytext"]
        ,bad_tags="form style script meta"
        ,bad_classes="")

thn21_com = xpath_extractor_factory(
        css_selectors=["#V , .ti"]
        ,bad_tags="form style script meta"
        ,bad_classes="")

def vjmedia_upto_author(elem):
    for x in elem.getparent().iterchildren():
        if x == elem:
            return False
        elif x.get('id') == 'author-spotlight':
            break
    return True

vjmedia_com_hk = xpath_extractor_factory(
        css_selectors=[".hentry"]
        ,is_bad=vjmedia_upto_author)

###################################
# Main modules
#

def collect_features(browser):
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
        isgood     = 1 if visible and xpath in content_xpaths else 0
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
    from debugger import debugExceptions
    debugExceptions()
    logging.basicConfig(level=logging.INFO  # level DEBUG will be noisy with selenium
                       ,format='%(asctime)-15s %(levelname)s:%(name)s:%(message)s')
    main()

# vim:set nowrap et ts=4 sw=4:
