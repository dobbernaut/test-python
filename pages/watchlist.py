import re

from pages.watchlist_elements import WatchlistElements
from base_selenium_page import BasePage
import config


class Watchlist(BasePage):

    def __init__(self, browser):
        self.watchlist = WatchlistElements()
        BasePage.__init__(self, browser)

    def get_listings_on_watchlist(self):
        self.wait_for_watchlist_form()
        listings = []
        for index, watchlist_listing in enumerate(self.watchlist.listings_checkbox()):
            listings.append({
                'index': index,
                'listing_id': self.get_listing_id_from_checkbox(watchlist_listing)
            })
        return listings

    def remove_listings_from_watchlist(self, listings_details):
        self.wait_for_watchlist_form()
        for listing in listings_details:
            for watchlist_listing in self.watchlist.listings_checkbox():
                watchlist_listing_id = self.get_listing_id_from_checkbox(watchlist_listing)
                if watchlist_listing_id == listing['listing_id']:
                    watchlist_listing.click()
                    break
            else:
                raise ValueError(f'Listing "{listing}" is not on watchlist')
        self.delete_selected_listings()

    def delete_selected_listings(self):
        self.watchlist.delete.click()
        self.watchlist.confirm_deletion.click()

    def get_listing_id_from_checkbox(self, listing_element):
        return int(re.search('[^(chk)]\\d*', listing_element.get_attribute('name')).group(0))

    def wait_for_watchlist_form(self):
        self.watchlist.watchlist_form()
