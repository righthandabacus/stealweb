#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import logging
import urlparse
import urllib
import re
from lxml import etree

def configLogger(quiet=False, debug=False, filename=None, root=''):
    '''
    Configurating the logging facilities to log to both console and file

    Args:
        quiet (bool): turn off console logging when true
        debug (bool): console logging level will set to debug when true, info otherwise
        filename (str): if set, log will also be written to this file, at debug level and above
        root (str): the root logger to set, default to empty string
    '''
    if quiet:
        logging.getLogger(root).addHandler(logging.NullHandler())
    else:
        # Set up console logger, with ANSI escape for colouring
        # See http://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output
        RESET_SEQ = "\033[0m"
        COLOUR_SEQ = "\033[1;%dm"
        BOLD_SEQ = "\033[1m"
        (BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE) = range(30,38)
        COLOURS = {'DEBUG':BLUE, 'INFO':CYAN, 'WARNING':YELLOW, 'CRITICAL':MAGENTA, 'ERROR':RED}
        class ColouredFormatter(logging.Formatter):
            def __init__(self, msg):
                logging.Formatter.__init__(self, msg)
            def format(self, record):
                s = logging.Formatter.format(self, record)
                if record.levelname in COLOURS:
                    s = (COLOUR_SEQ % COLOURS[record.levelname]) + s + RESET_SEQ
                return s
        shandler = logging.StreamHandler()
        shandler.setLevel(logging.DEBUG if debug else logging.INFO)
        shandler.setFormatter(ColouredFormatter('%(name)s(%(lineno)d):%(levelname)s:%(message)s'))
        logging.getLogger(root).addHandler(shandler)
    if filename:
        # Set up file logger
        fhandler = logging.FileHandler(filename, encoding='utf8')
        fhandler.setLevel(logging.DEBUG)
        fhandler.setFormatter(
            logging.Formatter('%(asctime)s:%(name)s(%(lineno)d):%(levelname)s:%(message)s', '%Y-%m-%d %H.%M.%S'))
        logging.getLogger(root).addHandler(fhandler)
    logging.getLogger(root).setLevel(logging.DEBUG)

def escape_url(url):
    '''Convert UTF8-characters-bearing URL into IRI - by HTML quoting non-ASCII parts

    Args:
        url (str): URL parsable by urlparse

    Returns:
        str: URL same as input with UTF8 characters replaced by URL-encoded counterparts
    '''
    urlparts = list(urlparse.urlparse(url))
    for i in [2,3,4]:
        if urlparts[i]:
            urlparts[i] = urllib.quote(urlparts[i])
    return urlparse.urlunparse(urlparts)

def condense_space(string):
    '''Replace consecutive multiple spaces in string with single space
    '''
    if not isinstance(string,basestring):
        return ''
    string = string.replace(u'\u2028', ' ') # U+2028 = line separator
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
    '''assume a rgba value put on top of white background, find the resulting
    rgb value. See <https://en.wikipedia.org/wiki/Alpha_compositing>
    '''
    if len(rgba) == 3: return rgba # pass-thou if no alpha channel
    white = [255, 255, 255]
    rgb = rgba[:3]
    alpha = rgba[3]
    return [alpha*fg+(1.0-alpha)*bg for fg,bg in zip(rgb,white)]

def luminance(rgb):
    '''find luminance from rgba color using BT.709 standard, formula:
    Y = (0.2126R+0.7152G+0.0722B)*alpha assume all elements are put on top of
    white background. See <https://en.wikipedia.org/wiki/YUV>
    '''
    Y = sum(coeff*color for coeff,color in zip([0.2126,0.7152,0.0722],rgb))
    return Y

def html2dom(htmlstr):
    parser = etree.HTMLParser(remove_blank_text=True, remove_comments=True, remove_pis=True)
    domtree = etree.fromstring(htmlstr, parser)
    return etree.ElementTree(domtree)

gethost = lambda url: urlparse.urlparse(url).netloc

def samedomain(domain1, domain2):
    "Given two host names, tell if they are in the same domain"
    assert(isinstance(domain1,basestring) and isinstance(domain2,basestring))
    part1 = reversed(filter(None,domain1.lower().split('.')))
    part2 = reversed(filter(None,domain2.lower().split('.')))
    assert(part1 and part2)
    return all(a==b for a,b in zip(part1, part2))

any2unicode = lambda s: s.decode('utf-8') if isinstance(s,str) else unicode(s) if not isinstance(s,unicode) else s
str2unicode = lambda s: s.decode('utf-8') if isinstance(s,str) else s
