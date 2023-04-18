from pages.base_page import BasePage
from locators.search_page_locators import SearchPageLocators as Locators

class SearchPage(BasePage):

    def get_number_of_results_header(self):
        text = self.element_is_visible(Locators.NUMBER_OF_RESULTS_HEADER).text
        return int(text[0:3])

    def get_persons_locations(self):
        location = self.elements_are_visible(Locators.PERSON_LOCATION)
        text = [i.text for i in location]
        return text