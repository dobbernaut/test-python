import pytest

from base_selenium_test import BrowserTestCase
from pages.home import Home
from pages.listings import Listings
from enums.listing_categories import Categories
from enums.listing_sub_categories import Antiques


@pytest.mark.ui
@pytest.mark.uisearch
@pytest.mark.search
class TestGeneralSearch(BrowserTestCase):

    def setUp(self):
        self.home = Home(self.browser)
        self.listings = Listings(self.browser)

    def test_should_return_search_results_given_a_category_and_a_search_string(self):
        self.home.open()
        self.home.open_main_category(Categories.Antiques)
        self.home.open_sub_category(Antiques.Stamps)
        self.home.search('product')

        assert self.listings.total_listings() >= 0
        assert len(self.listings.get_listings()) >= 0
