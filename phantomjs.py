from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class phantomjs(object):
    def __init__(self, width=1920, height=1080):
        # PhantomJS config, override user agent string and bug workaround
        DCAP = dict(DesiredCapabilities.PHANTOMJS)
        DCAP.update({
            "phantomjs.page.settings.userAgent":
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 (KHTML, like Gecko) Chrome/15.0.87"
           ,"phantomjs.page.settings.loadImages": True
        })
        self.browser = webdriver.PhantomJS(desired_capabilities=DCAP)
        self.browser.set_window_size(width, height)
        #self.browser.implicitly_wait(10) # seconds

    def __del__(self):
        import signal
        self.browser.service.process.send_signal(signal.SIGTERM) # kill the specific phantomjs child proc
        self.browser.quit()     

    def __getattr__(self, name):
        return getattr(self.browser, name)

    def wait_until_staled(self, element, timeout=30):
        WebDriverWait(self.browser, timeout).until(staleness_of(element))

    def get_xpath(self, element):
        js = '''
            // adapted from http://stackoverflow.com/questions/2631820/im-storing-click-coordinates-in-my-db-and-then-reloading-them-later-and-showing/2631931#2631931
            var getXPathTo = function (element){
                /* -- if we allow id() in XPath
                if (element.id !== '')
                    return 'id("' + element.id + '")';
                */
                // Recursion breaker: at document root
                if (element === document)
                    return '';
                // Recursively find path of this element by counting siblings
                var count = 0;
                var hit = 0;
                var siblings = element.parentNode.childNodes;
                for (var i=0; i<siblings.length; i++) {
                    if (siblings[i].nodeType===1 && siblings[i].tagName===element.tagName)
                        count++;
                    if (siblings[i] === element)
                        hit = count;
                    if (count > 1 && hit >= 1)
                        break;
                };
                // Return XPath
                if (hit == 1 && count == 1) {
                    return getXPathTo(element.parentNode)+'/'+element.tagName.toLowerCase();
                } else {
                    return getXPathTo(element.parentNode)+'/'+element.tagName.toLowerCase()+'['+hit+']';
                };
            };
            return getXPathTo(arguments[0]);
        '''
        ret = self.browser.execute_script(js, element)
        return ret
