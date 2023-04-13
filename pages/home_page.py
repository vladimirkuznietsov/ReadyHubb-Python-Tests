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
