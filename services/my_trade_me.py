import requests

from base_service import BaseService
import config


class MyTradeMe(BaseService):

    def retrieve_watchlist(self, filter='All'):
        return requests.get(
            f'{config.site_urls["api"]}/mytrademe/watchlist/{filter}.json',
            headers={'authorization': self.member_authentication()}
        )

    def add_listing_to_watchlist(self, listing_id):
        return requests.post(
            f'{config.site_urls["api"]}/mytrademe/watchlist/{listing_id}.json',
            headers={'authorization': self.member_authentication()}
        )

    def remove_listing_from_watchlist(self, listing_id):
        return requests.delete(
            f'{config.site_urls["api"]}/mytrademe/watchlist/{listing_id}.json',
            headers={'authorization': self.member_authentication()}
        )
