#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import argparse
import codecs
import contextlib
import logging
import os
import re
import sys

from utf8csv import csv,UnicodeReader

logger = logging.getLogger('reader')

###################################
# Helper functions
#

def walkdir(rootdir, condition=lambda name:name.lower().endswith('.csv')):
    '''
    Walk the dir, return path to each file fulfilling a condition. Default to find all *.csv files
    '''
    for path, dirs, files in os.walk(rootdir):
        dirs.sort()
        for name in sorted(files):
            if condition(name):
                yield os.path.join(path, name)

@contextlib.contextmanager
def smart_open(filename=None, mode='wb'):
    '''
    https://stackoverflow.com/questions/17602878/how-to-handle-both-with-open-and-sys-stdout-nicely/17603000
    '''
    fh = open(filename, mode) if filename and filename != '-' else sys.stdout
    try:
        yield fh
    finally:
        if fh is not sys.stdout:
            fh.close()

class colour(object):
    '''
    To hold a colour tuple and support conversiopn into luminance value
    '''
    def __init__(self, code='rgb(0,0,0)'):
        if not code.strip():
            self.type = None
            self.values = tuple()
        else:
            try:
                m = re.match(r'(\w+)\((([\d\.]+,)+[\d\.]+)\)', re.sub(r'\s','',code or ''))
                self.type = m.group(1).lower()
                self.values = tuple(float(x) for x in m.group(2).split(','))
            except:
                raise ValueError
    def __repr__(self):
        return '%s<%s>' % (self.type.upper() , ','.join(str(v) for v in self.values))
    def rgb(self):
        "convert rgba into rgb color, assume it is over a white background"
        if self.type == 'rgb':
            return self
        elif self.type == 'rgba':
            assert(len(self.values) == 4)
            white = [255,255,255]
            rgb = self.values[:3]
            alpha = self.values[3]
            self.values = tuple([alpha*fg+(1.0-alpha)*bg for fg,bg in zip(rgb,white)])
            self.type = 'rgb'
            return self
        else:
            raise NotImplementedError
    def get_y(self):
        '''
        find luminance from rgba color using BT.709 standard, formula: Y = (0.2126R+0.7152G+0.0722B)*alpha
        assume all elements are put on top of white background
        ref: https://en.wikipedia.org/wiki/YUV
        '''
        self.rgb()
        Y = sum(coeff*color for coeff,color in zip([0.2126,0.7152,0.0722],self.values))
        return Y

def guesstype(string):
    'Given string, guess what is it'
    if not (string or '').strip():
        return None # empty
    try:
        return int(string) # like int, pos or neg
    except:
        pass
    try:
        return float(string) # like float, inf included
    except:
        pass
    try:
        assert(string.lower().startswith('rgb(') or string.lower().startswith('rgba('))
        return colour(string) # like rgba(0,0,0,0)
    except:
        pass
    try:
        return str(string) # convertible to string
    except:
        pass
    return string # unicode, most likely

def readcsv(filename):
    'Open and read CSV file, return 2D array with best-effort data type conversion'
    # open file and read
    with open(filename, "rb") as csvfile:
        if csvfile.read(3) != codecs.BOM_UTF8:
            csvfile.seek(0) # skip BOM if exists
        csvin = UnicodeReader(csvfile) # assume all data are UTF8
        table = [[guesstype(cell) for cell in row] for row in csvin]
        return table

def binary_search(data, comparer):
    '''
    Given array data, find the interested item using binary search

    Args:
        data (list): is a list object with len() and random access supported
        comparer (callable): is a function that given a list element, return 0 if search
           is found, +ve if should go to higher index, -ve if should go to lower index
    Returns:
        None if not found or otherwise the index to the array
    '''
    head = 0
    tail = len(data) - 1
    # corner case check
    hint = comparer(data[head])
    if hint == 0:
        return head # found!
    elif hint < 0 or head==tail:
        return None # no way we can find in this array
    hint = comparer(data[tail])
    if hint == 0:
        return tail # found!
    elif hint > 0:
        return None # no way we can find in this array
    while True:
        mid = (head + tail) // 2
        if mid == head or mid == tail:
            return None # nothing more to check and not yet found anything
        hint = comparer(data[mid])
        if hint == 0:
            return mid # found!
        elif hint > 0:
            head = mid
        else:
            tail = mid
        assert(head <= tail)

def derivedata(csvfile):
    '''
    Read from one CSV file, and derive secondary features

    Returns:
      list: list of dict of element attributes

    Data dictionary of keys in each dict:
      tagname     [str] HTML tag name
      xpath*      [str] xpath of element
      depth*      [int] node count to its deepest descendent in dom tree
      childcount  [int] num of children
      width       [int] pixel width of element's bounding box
      height      [int] pixel height of element's bounding box
      x           [int] pixel coordinate of left edge of element's bounding box to the page
      y           [int] pixel coordinate of top edge of element's bounding box to the page
      xpct        [float] percentage position of element's left edge to window width
      ypct        [float] percentage position of element's top edge to page height
      area        [int] area of element's bounding box in pixels
      areapct*    [float] percentage area of element's bounding box to area of page
      fglum       [int] foreground colour luminance
      bglum       [int] background colour luminance
      sourcepct   [float] percentage position of source line in HTML
      pospct      [float] percentage postiion of node in the DOM
      htmllen     [int] character length of HTML code
      textlen     [int] character length of text
      textxws     [int] character length of text excluding whitespaces
      textself    [int] character length of text directly inside this element
      textpct0    [float] ratio of text excluding whitespaces (in chars) to HTML code
      textpct1    [float] ratio of text (in chars) to HTML code
      textpct2    [float] ratio of text excluding whitespaces directly inside this element (in chars) to HTML code
      visible     [bool] visibility of this element
      goodness*   [bool] is this part of main content
    items except those with * has par-version for the element's parent
    '''
    # read CSV data with header
    rows = readcsv(csvfile)
    header = rows[0]
    rows = rows[1:]
    assert(all(k in header for k in # TODO fontsize significant?
                   ("id parent tagname depth childcount sourceline sourcepct pospct xpct x y width height "
                    "fgcolor bgcolor textxws textlen htmllen visible xpath textclip goodness").split()))
    # define data retriever
    _lookup = {h:i for i,h in enumerate(header)}
    cell = lambda row, col: row[_lookup[col]]
    xpathtok = lambda xpathstr: [re.sub(r'\[\d+\]','',x) for x in xpathstr.split('/') if x] # tokenize components
    # remember page-wide features
    rows = filter(lambda row:cell(row,'xpath').startswith('/html/body') or cell(row,'xpath')=='/html', rows) # keep only those elements in HTML body
    maxheight = max(cell(row,'height') + cell(row,'y') for row in rows) # scan for largest dimension, more accurate than <html> or <body>
    htmlelem = next(row for row in rows if cell(row,'xpath')=='/html') # must exist
    bodyelem = next(row for row in rows if cell(row,'xpath')=='/html/body') # must exist
    bodywidth = max(cell(bodyelem,'width'), cell(htmlelem,'width'))
    # collect features that come directly from the element
    data = {}
    for row in rows:
        # copied over
        features = {key:cell(row,key) for key in
                      ('parent tagname depth childcount sourcepct pospct xpct x y width height '
                       'textxws textlen htmllen visible goodness').split()}
        # other derived features
        features['ypct'] = cell(row,'y')/maxheight # percentage position in page by geometry
        features['area'] = features['width'] * features['height']
        features['areapct'] = features['area']/(maxheight*bodywidth)
        features['textpct1'] = features['textlen']/features['htmllen'] # count with space
        features['textpct0'] = features['textxws']/features['htmllen'] # count without space
        features['fglum'] = cell(row,'fgcolor').get_y()
        features['bglum'] = cell(row,'bgcolor').get_y()
        features['xpath'] = " ".join(sorted(set(xpathtok(cell(row,'xpath')))))
        if features['textlen']==0 and features['tagname'] not in ['a','br','img']:
            features['goodness'] = 0
        data[cell(row,'id')] = features
    # collect features of children to deduce portion of text directly belong to the element
    for elemid in data:
        children = filter(lambda f:f['parent']==elemid, data.itervalues())
        totaltext = sum(f['textxws'] for f in children if f['visible'])
        data[elemid]['textself'] = data[elemid]['textxws'] - totaltext # num of text bytes immediately inside this element
        data[elemid]['textpct2'] = data[elemid]['textself']/data[elemid]['htmllen'] # count only text belong to itself
    # collect features of parents
    for features in data.itervalues():
        if features['parent'] not in data: continue
        parent = data[features['parent']]
        # copy features
        keys = ("tagname childcount sourcepct pospct x y xpct ypct width height area fglum bglum visible "
                "textself textxws textlen htmllen textpct0 textpct1 textpct2 ").split()
        features.update({'par'+k:parent[k] for k in keys})
    # return
    return filter(lambda x:'partagname' in x, data.values())

###################################
# main program
#

def parseargs():
    parser = argparse.ArgumentParser(
        description='Read DOM features in CSV files, derive secondary features from them, output training '
                    'data in one CSV'
        ,formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-d", dest='dir', nargs='*', help="directory to find CSV files")
    parser.add_argument("-f", dest='csv', nargs='*', help="path to a single CSV file")
    parser.add_argument("-o", dest='output', help="output CSV filename, default is to stdout")
    parser.add_argument("-v", dest="verbose", action='store_true', default=False, help="show debug message")
    args = parser.parse_args()
    return args

def main():
    args = parseargs()
    logger.setLevel(logging.DEBUG if args.verbose else logging.INFO)
    # collect input files in a list
    csvfiles = args.csv or []
    for dirname in (args.dir or []):
        csvfiles.extend(list(walkdir(dirname)))
    # collect output features from each CSV
    data = []
    for f in csvfiles:
        data.extend(derivedata(f))
    if not data:
        logger.error('No data collected')
        return
    # add one-hot encoding of textual data: xpath, tagname, partagname
    allxpath   = list(sorted(reduce(lambda x,y:y | x, [f['xpath'] for f in data], set([]))))
    alltags    = list(sorted(reduce(lambda x,y:y | x, [set([f['tagname']]) for f in data], set([]))))
    allpartags = list(sorted(reduce(lambda x,y:y | x, [set([f['partagname']]) for f in data], set([]))))
    for row in data:
        xpath, tag, partag = row['xpath'], row['tagname'], row['partagname']
        del row['xpath']
        del row['tagname']
        del row['partagname']
        for t in allxpath:
            row['xpath_has_'+t] = 1 if t in xpath else 0
        for t in alltags:
            row['tag_is_'+t] = 1 if tag==t else 0
        for t in allpartags:
            row['partag_is_'+t] = 1 if partag==t else 0
    # convert data into CSV output
    header = ['goodness'] + sorted([k for k in data[0].keys() if k != 'goodness'])
    table = [header] + [
        [row[k] for k in header]
        for row in data
    ]
    # write output as CSV
    with smart_open(args.output, 'wb') as csvfile:
        csvout = csv.writer(csvfile) # do not need UnicodeWriter here as all textual elements are removed
        csvout.writerows(table)

if __name__ == '__main__':
    from debugger import debugExceptions
    debugExceptions()
    logging.basicConfig(format='%(asctime)-15s %(levelname)s:%(name)s:%(message)s')
    main()

# vim:set sts=4 ts=4 sw=4 bs=2 et:
