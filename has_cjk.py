#!/usr/bin/env python

# Check if any CJK character on the specified file
#

import sys

def codestat(s):
    latin = cjk = other = 0
    for c in s:
        codepoint = ord(c)
        if codepoint <= 0x2AF:
            latin += 1
        elif 0x2E80 <= codepoint <= 0x9FFF:
            cjk += 1
        else:
            other += 1
    return dict(latin=latin, cjk=cjk, other=other)

def has_cjk(filename):
    s = open(filename).read().decode('utf8')
    return codestat(s)['cjk'] > 0

if __name__ == '__main__':
    print has_cjk(sys.argv[1])
