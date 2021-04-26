from pages.home_elements import HomeElements
from base_selenium_page import BasePage
import config


class Home(BasePage):

    def __init__(self, browser):
        self.home = HomeElements()
        BasePage.__init__(self, browser)

    def log_in(self, role_details):
        self.open_url(config.site_urls['ui'])
        self.home.open_login.click()
        self.home.email.set_value(role_details['username'])
        self.home.password.set_value(role_details['password'])
        self.home.login.click()
        self.home.logout()

    def log_out(self):
        self.home.logout.click()
        self.home.open_login()

    def open(self):
        self.open_url(config.site_urls['ui'])

    def search(self, search):
        self.home.search_box.set_value(search)
        self.home.search.click()
        self.home.search_results_heading()

    def toggle_watchlist_dropdown(self):
        self.home.open_watchlist_dropdown.click()
        self.home.watchlist_dropdown()

    def view_watchlist(self):
        self.toggle_watchlist_dropdown()
        self.home.view_watchlist.click()

    def open_main_category(self, category):
        self.home.main_category()
        for main_category in self.home.main_categories():
            if main_category.text == category:
                main_category.click()
                break
        else:
            raise ValueError(f'Category "{category}" was not found from main categories')

    def open_sub_category(self, category):
        self.home.subcategory()
        for subcategory in self.home.subcategories():
            if subcategory.text == category:
                subcategory.click()
                break
        else:
            raise ValueError(f'Subcategory "{category}" was not found from main Subcategory')
