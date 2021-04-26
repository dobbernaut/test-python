import pytest

from base_selenium_test import BrowserTestCase
from pages.home import Home
from pages.listings import Listings
from pages.watchlist import Watchlist
from enums.listing_categories import Categories
from enums.listing_sub_categories import Antiques
import config


@pytest.mark.ui
@pytest.mark.uiwatchlist
@pytest.mark.watchlist
class TestWatchlist(BrowserTestCase):

    def setUp(self):
        self.listings_to_remove = []
        self.home = Home(self.browser)
        self.listings = Listings(self.browser)
        self.watchlist = Watchlist(self.browser)

        self.home.log_in(config.roles['test_role'])

    def tearDown(self):
        self.watchlist.remove_listings_from_watchlist(self.listings_to_remove)
        self.home.log_out()

    def test_should_add_a_listing_to_the_user_watchlist(self):
        self.home.open_main_category(Categories.Antiques)
        self.home.open_sub_category(Antiques.Stamps)
        self.home.search('product')
        listing_to_add = self.listings.get_listings()[0]
        self.listings_to_remove.append(listing_to_add)

        self.listings.add_listing_to_watchlist({'listing_id': listing_to_add['listing_id']})
        self.home.view_watchlist()
        assert any([listing for listing in self.watchlist.get_listings_on_watchlist()
                    if listing['listing_id'] == listing_to_add['listing_id']])
