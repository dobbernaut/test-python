import unittest
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

import config


class Browser(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Browser, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        # options = Options()
        # self.profile = webdriver.FirefoxProfile()
        # self.profile.set_preference("general.useragent.override", self.user_agent)
        # self.profile.set_preference('browser.cache.memory.enable', False)
        # self.profile.set_preference('browser.cache.disk.enable', False)
        # self.profile.set_preference('browser.cache.offline.enable', False)
        # self.profile.set_preference('network.http.use-cache', False)
        # self.profile.set_preference('browser.cache.disk.parent_directory', '/tmp')
        # self.profile.set_preference("webdriver.log", "/tmp/firefox_console")
        # options.add_argument("--headless")
        # self.browser = webdriver.Firefox(options=options)
        # self.browser.set_window_size(1280, 1024)

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-logging')
        options.add_argument('--log-level=2')
        options.add_argument('--disk-cache-dir=/tmp')
        options.add_argument('--window-size=1280,1024')
        self.browser = webdriver.Chrome(options=options)


class BrowserTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(BrowserTestCase, cls).setUpClass()
        cls.browser = Browser().browser
        cls.browser.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.browser.delete_all_cookies()
        cls.browser.quit()
        super(BrowserTestCase, cls).tearDownClass()
