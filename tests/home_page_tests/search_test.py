import time

from pages.home_page import HomePage
from pages.search_page import SearchPage
from data.data import Data

class TestSearch:

    def test_search_by_location(self, driver):
        home_page = HomePage(driver)
        search_page = SearchPage(driver)

        home_page.fill_search_field(Data.location)
        home_page.select_first_location_option()
        assert len(search_page.get_persons_locations()) == search_page.get_number_of_results_header()
        for i in search_page.get_persons_locations():
            assert 'GA', 'USA' in i
