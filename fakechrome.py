#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Fake Chrome browser using CEF for reading a webpage
from __future__ import print_function
import json
import logging
import os
import sys
import threading
import time
from cefpython3 import cefpython as cef

sys.excepthook = cef.ExceptHook # shutdown CEF processes on exception
logger = logging.getLogger('fc')

class fakechromehandlers(object):
    '''
    Handler object
    '''
    __slots__ = ('chrome',)
    def __init__(self, fakechrome):
        self.chrome = fakechrome

    def GetViewRect(self, rect_out, **kwargs):
        "RenderHandler interface. CEF will call this to read what geometry should the browser be"
        logger.debug('Reset view rect')
        rect_out.extend([0, 0, self.chrome.width, self.chrome.height]) # [x, y, width, height]
        return True

    def OnConsoleMessage(self, browser, message, **kwargs):
        "DisplayHandler interface. Intercept all message printted to console"
        logger.warning("[console] %s" % message)

    def OnLoadError(self, browser, frame, error_code, failed_url, **_):
        self.chrome.ready = error_code # like True
        logger.debug('Load Error')
        self.chrome._getReadyLock.acquire()
        self.chrome._getReadyLock.notify()
        self.chrome._getReadyLock.release()

    def OnLoadingStateChange(self, browser, is_loading, **kwargs):
        "LoadHandler interface. Browser will call when load state change"
        if not is_loading:
            # Loading is complete. DOM is ready.
            self.chrome.ready = True
            logger.debug('Loaded')
            self.chrome._getReadyLock.acquire()
            self.chrome._getReadyLock.notify()
            self.chrome._getReadyLock.release()
        else:
            logger.debug('Loading')
            self.chrome.ready = False

class fakechrome(object):
    # https://stackoverflow.com/questions/472000/usage-of-slots
    __slots__ = ('width','height','headless','browser','source','domArray'
                ,'windowParams','ready','_handler','__weakref__' # weakref for StringVisitor iface
                ,'_getSourceLock','_getDOMLock','_getReadyLock')

    def __init__(self, width=1920, height=1080, headless=False):
        self.width = width
        self.height = height
        self.headless = headless

        # pointer to reusable CEF objects
        self.browser = None
        self.source = None
        self.domArray = None
        self.windowParams = None
        self.ready = True
        self._getSourceLock = threading.Condition()
        self._getDOMLock = threading.Condition()
        self._getReadyLock = threading.Condition()
        self._handler = fakechromehandlers(self)

        settings = {
            'user_agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) ' \
                         'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                         'Chrome/64.0.3282.140 Safari/537.36'
        }
        if self.headless:
            settings['windowless_rendering_enabled'] = True
        cef.Initialize(settings=settings)

    def __getattr__(self, name):
        # all unknown attributes/methods will pass through to CEF browser
        return getattr(self.browser, name)

    def getBrowser(self):
        if self.browser:
            return self.browser
        # create browser instance
        if self.headless:
            parent_handle = 0
            winfo = cef.WindowInfo()
            winfo.SetAsOffscreen(parent_handle)
            self.browser = cef.CreateBrowserSync(window_info=winfo)
        else:
            self.browser = cef.CreateBrowserSync()
        # create bindings for DOM walker and handler for browser activities
        self.browser.SetClientHandler(self._handler) # use render handler to resize window
        self.browser.SendFocusEvent(True) # put browser in focus
        self.browser.WasResized() # need to call this at least once in headless mode
        bindings = cef.JavascriptBindings(bindToFrames=False, bindToPopups=True)
        bindings.SetFunction("get_attr_callback", self._domWalkerCallback)
        self.browser.SetJavascriptBindings(bindings)
        logger.debug('Browser created')
        return self

    def run(self):
        "Launch message loop, block until returns"
        logger.debug('Running message loop')
        cef.MessageLoop()
        logger.debug('Message loop end!')

    def LoadUrl(self, url, synchronous=False):
        "Load a URL, pass-through to CEF browser"
        self.ready = False # safe-guard the wait below
        self.browser.LoadUrl(url)
        logger.debug('Waiting for %s to load' % url)
        if synchronous:
            self._getReadyLock.acquire()
            if not self.ready:
                self._getReadyLock.wait() # sleep until browser status update, no timeout
            self._getReadyLock.release()

    def getSource(self, synchronous=False):
        'Get HTML source code of the main frame asynchronously. Handled by self.Visit() when ready'
        self.source = None
        self.browser.GetMainFrame().GetSource(self)
        logger.debug('Waiting for HTML source ready')
        if synchronous:
            self._getSourceLock.acquire()
            if not self.source:
                self._getSourceLock.wait() # sleep until Visit() populated self.source, no timeout
            self._getSourceLock.release()
        return self.source

    def _domWalkerCallback(self, array, windowparams=None):
        "Bound to Javascript as callback function for DOM walker"
        logger.debug('DOM walker called back')
        self.domArray = array
        self.windowParams = windowparams
        self._getDOMLock.acquire()
        self._getDOMLock.notify()
        self._getDOMLock.release()

    def getDOMdata(self, synchronous=False):
        self.domArray = None
        js_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),"cef_walkdom.js")
        js_code = open(js_path).read()
        threading.Timer(0, self.browser.GetMainFrame().ExecuteJavascript, [js_code]).start()
        logger.debug('Waiting for DOM data ready')
        if synchronous:
            self._getDOMLock.acquire()
            if self.domArray is None:
                self._getDOMLock.wait() # sleep until JS code callback set self.domArray, no timeout
            self._getDOMLock.release()
        return self.domArray

    def Visit(self, value):
        "StringVisitor interface. GetSource() will call this function with browser's source HTML"
        self.source = value
        self._getSourceLock.acquire()
        self._getSourceLock.notify()
        self._getSourceLock.release()

if __name__ == '__main__':
    import argparse
    import json
    logging.basicConfig(format='%(asctime)-15s %(levelname)s:%(name)s:%(message)s')
    parser = argparse.ArgumentParser(
                description='CEF-based web crawler and DOM analyser'
               ,formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("url", help="URL to crawl")
    parser.add_argument("-d", dest="domjson", default='dom.json', help="file to save the DOM data")
    parser.add_argument("-s", dest="srchtml", default="source.html", help="file to save the srouce HTML")
    parser.add_argument("-l", dest="headless", action='store_true', default=False, help="use CEF headlessly")
    parser.add_argument("-v", dest="verbose", action='store_true', default=False, help="show debug message")
    args = parser.parse_args()
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    browser = fakechrome(width=640, height=480, headless=args.headless).getBrowser()
    def main():
        browser.ready = False
        browser.LoadUrl(args.url, True) # True = synchronous call
        with open(args.srchtml, 'w') as srcfp:
            source = browser.getSource(True) # synchronous get
            assert(source)
            srcfp.write(source)
            logger.debug('Wrote to %s' % args.srchtml)
        with open(args.domjson, 'w') as domfp:
            dom = browser.getDOMdata(True) # synchronous get
            assert(dom)
            domfp.write(json.dumps(dom, indent=2))
            logger.debug('Wrote to %s' % args.domjson)
        browser.CloseBrowser()
    mainthread = threading.Thread(target=main)
    mainthread.start()
    browser.run() # blocking until browser closed
    mainthread.join()
    browser = None
    cef.Shutdown()
