import time

from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators as Locators


class HomePage(BasePage):
    expected_account_dropdown_options = ['Bookings', 'Favorites', 'My profile']

    def click_sign_in_button(self):
        self.element_is_visible(Locators.SIGN_IN_BUTTON).click()

    def click_account_button(self):
        self.element_is_visible(Locators.ACCOUNT_BUTTON).click()
        options = self.elements_are_visible(Locators.ACCOUNT_OPTIONS)
        texts = [i.text for i in options]
        return texts

    def fill_search_field(self, location):
        self.element_is_visible(Locators.SELECT_LOCATION_INPUT).click()
        self.element_is_visible(Locators.SELECT_LOCATION_INPUT).send_keys(location)

    def select_first_location_option(self):
        self.element_is_visible(Locators.SEARCH_FIRST_OPTION).click()

    def click_account_option(self, index):
        buttons = self.elements_are_visible(Locators.ACCOUNT_OPTIONS)
        buttons[index].click()
