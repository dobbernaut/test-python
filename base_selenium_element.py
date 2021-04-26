from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from base_selenium_browser import Browser
import config


class Elements(Browser):

    def set_browser(self, browser):
        for element in self.__dict__.values():
            if isinstance(element, Element):
                element.set_browser(browser)


class Element(Browser):

    def __init__(self, locator):
        self.locator = locator
        self.is_xpath_locator = locator.startswith('//')

    def __call__(self):
        if self.is_xpath_locator:
            WebDriverWait(self.browser, config.selenium_wait_time).until(
                lambda driver: len(driver.find_elements_by_xpath_selector(self.locator)),
                f'URL: {self.browser.current_url} | Waiting for {self.locator}, but did not show up in time'
            )
            return self.browser.find_elements_by_xpath_selector(self.locator)
        else:
            WebDriverWait(self.browser, config.selenium_wait_time).until(
                lambda driver: len(driver.find_elements_by_css_selector(self.locator)),
                f'URL: {self.browser.current_url} | Waiting for {self.locator}, but did not show up in time'
            )
            return self.browser.find_elements_by_css_selector(self.locator)

    def click(self, index=0):
        element = self()[index]
        self.scroll_into_view(index)
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()
        actions.click().perform()

    def set_value(self, value, index=0):
        element = self()[index]
        self.scroll_into_view(index)
        element.clear()
        element.send_keys(value)

    def send_key(self, key):
        actions = ActionChains(self.browser)
        actions.key_down(key)
        actions.perform()

    def scroll_into_view(self, index=0):
        self.browser.execute_script('arguments[0].scrollIntoView(false)', self()[index])

    def move_to(self, index=0):
        actions = ActionChains(self.browser)
        actions.move_to_element(self()[index])
        actions.perform()
