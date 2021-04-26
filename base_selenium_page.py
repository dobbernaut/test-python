from base_selenium_browser import Browser
from base_selenium_element import Elements


class BasePage(Browser):

    def __init__(self, browser):
        self.browser = browser
        for value in self.__dict__.values():
            if isinstance(value, Elements):
                value.set_browser(browser)

    def open_url(self, url):
        self.browser.get(url)
