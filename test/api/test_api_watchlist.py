import pytest
import unittest

from services.search import Search
from services.my_trade_me import MyTradeMe
from json_to_dictionary import JSONToDictionary


@pytest.mark.api
@pytest.mark.apiwatchlist
@pytest.mark.watchlist
class TestWatchlist(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.search = Search()
        cls.my_trade_me = MyTradeMe()

        response = cls.search.general('0187-4383-', 'product')
        if response:
            cls.listing_id = JSONToDictionary(response.text).List[0].ListingId
        if not cls.listing_id:
            pytest.fail('Watchlist tests cannot proceed if it fails to get a listing id')

    @classmethod
    def tearDownClass(cls):
        response = cls.my_trade_me.remove_listing_from_watchlist(cls.listing_id)
        assert response.status_code == 200
        data = JSONToDictionary(response.text)
        assert data.Success

    def test_should_add_a_listing_to_user_watchlist(self):
        response = self.my_trade_me.add_listing_to_watchlist(self.listing_id)
        assert response.status_code == 200

        data = JSONToDictionary(response.text)
        assert data.Success

    def test_should_have_the_added_listing_on_user_watchlist(self):
        response = self.my_trade_me.retrieve_watchlist()
        assert response.status_code == 200

        data = JSONToDictionary(response.text)
        assert any([listing for listing in data.List if listing.ListingId == self.listing_id])
