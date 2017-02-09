from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class phantomjs(object):
    # Use a lot of Javascript here
    # Reference: https://developer.mozilla.org/en-US/docs/Web/API

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
        # all unknown attributes/methods will pass through to selenium
        return getattr(self.browser, name)

    def wait_until_staled(self, element, timeout=30):
        WebDriverWait(self.browser, timeout).until(staleness_of(element))

    def get_everything(self):
        js = open('get_everything.js').read()
        ret = self.browser.execute_script(js)
        return ret

    def get_xpath(self, element):
        js = open('get_xpath.js').read()
        ret = self.browser.execute_script(js, element)
        return ret

    def get_all_attrs(self, element):
        js = '''
            var items = {};
            for (index = 0; index < arguments[0].attributes.length; ++index) {
                items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value
            };
            return items;
        '''
        ret = self.browser.execute_script(js, element)
        return ret

    def save_page_source(filename):
        open(filename, 'wb').write(self.browser.page_source.encode('utf8'))

    def save_rendered_html(filename):
        html = self.browser.execute_script('return document.documentElement.outerHTML;')
        open(filename, 'wb').write(html)
