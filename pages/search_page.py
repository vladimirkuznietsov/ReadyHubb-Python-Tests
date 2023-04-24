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

    def fill_search_field(self, location):
        self.element_is_visible(Locators.SELECT_LOCATION_INPUT).click()
        self.element_is_visible(Locators.SELECT_LOCATION_INPUT).send_keys(location)

    def select_first_location_option(self):
        self.element_is_visible(Locators.SEARCH_FIRST_OPTION).click()

    def click_person_card(self):
        self.element_is_visible(Locators.PERSON_CARD).click()

    def no_items_displayed(self):
        return self.element_is_present(Locators.NO_ITEMS_FOUND)

    def click_back_button(self):
        self.element_is_visible(Locators.BACK_BUTTON).click()

    def get_service_name(self):
        return self.element_is_visible(Locators.SERVICE_NAME).text

    def click_book_button(self):
        self.element_is_visible(Locators.BOOK_BUTTON).click()