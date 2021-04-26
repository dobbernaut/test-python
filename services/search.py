import requests

from base_service import BaseService
import config


class Search(BaseService):

    def general(self, category, search_string):
        return requests.get(
            f'{config.site_urls["api"]}/search/general.json',
            params={'category': category, 'search_string': search_string},
            headers={'authorization': self.app_authentication()}
        )
