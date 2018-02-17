#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import csv, codecs, cStringIO

class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        ln = self.reader.next().encode("utf-8")
        while ln[-1] not in ['\n','\r']:
            # There is issue with U+2028 (line separator; mandatory break)
            ln += self.reader.next().encode("utf-8")
        return ln

def skip_bom(f):
    """
    skip the BOM from a UTF8 file
    """
    header = f.read(3)
    if header != codecs.BOM_UTF8:
	f.seek(0)
    return f

class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self

class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

if __name__ == '__main__':
    import tabulate
    import argparse
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    parser = argparse.ArgumentParser(
                description='Print CSV as table to console'
               ,formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("csv", help="CSV file")
    parser.add_argument("-f", dest="format", default='plain', help="table "
            "format, any of: plain, simple, grid, fancy_grid, pipe, orgtbl, jira, "
            "presto, psql, rst, mediawiki, moinmoin, youtrack, html, latex, "
            "latex_raw, latex_booktabs, textile")
    args = parser.parse_args()
    with open(args.csv, "rb") as csvfile:
        csvin = UnicodeReader(skip_bom(csvfile))
        table = [row for row in csvin]
        print(tabulate.tabulate(table, headers="firstrow"))
