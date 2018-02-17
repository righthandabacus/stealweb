#!/usr/bin/env python
if __name__ == '__main__':
    from lxml import etree
    import sys
    print etree.tostring(
            etree.fromstring(
                open(sys.argv[1], 'rU').read(),
                parser = etree.HTMLParser(remove_blank_text=True, remove_comments=True, remove_pis=True)
            )
            ,encoding='utf8', pretty_print=True, method='xml'
        )
