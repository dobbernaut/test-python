import pytest
import unittest

from services.search import Search
from json_to_dictionary import JSONToDictionary


@pytest.mark.api
@pytest.mark.apisearch
@pytest.mark.search
class TestGeneralSearch(unittest.TestCase):

    def setUp(self):
        self.search = Search()

    def test_should_return_search_results_given_a_category_and_a_search_string(self):
        response = self.search.general('0187-4383-', 'product')
        assert response.status_code == 200

        data = JSONToDictionary(response.text)
        assert data.TotalCount >= 0
        assert len(data.List) >= 0
