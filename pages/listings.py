from pages.listings_elements import ListingsElements
from base_selenium_page import BasePage
import config


class Listings(BasePage):

    def __init__(self, browser):
        self.listings = ListingsElements()
        BasePage.__init__(self, browser)

    def total_listings(self):
        return int(self.listings.total_listings()[0].text)

    def get_listings(self):
        listings = []
        for index, listing in enumerate(self.listings.all_listings()):
            listings.append({
                'index': index,
                'listing_id': int(listing.get_attribute('data-listingid')),
                'title': self.listing_title(index)
            })
        return listings

    def add_listing_to_watchlist(self, listing_details):
        if not any([key for key in ['index', 'listing_id', 'title'] if key in listing_details]):
            raise AttributeError('No listing information provided. Provide either a listing title, id or index')

        for index, listing in enumerate(self.listings.all_listings()):
            if 'title' in listing_details and self.listing_title(index) == listing_details['title']:
                listing_found = True
            elif 'listing_id' in listing_details and int(listing.get_attribute('data-listingid')):
                listing_found = True
            elif 'index' in listing_details:
                listing_found = True
            if listing_found:
                self.add_to_watchlist(index)
                break
        else:
            raise ValueError(f'Failed to add listing {listing_details} to user watchlist')

    def listing_title(self, index):
        return self.listings.listings_title()[index].text

    def add_to_watchlist(self, index):
        self.listings.all_listings.move_to(index)
        self.listings.listings_add_to_watchlist.move_to(index)
        self.listings.listings_add_to_watchlist.click(index)
