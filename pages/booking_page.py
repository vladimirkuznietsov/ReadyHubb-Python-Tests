from pages.base_page import BasePage
from locators.booking_page_locators import BookingPageLocators as Locators


class BookingPage(BasePage):

    def get_no_bookings_header_text(self):
        return self.element_is_visible(Locators.NO_BOOKINGS_HEADER).text

    def click_search_button(self):
        self.element_is_visible(Locators.SEARCH_NEARBY_BUTTON).click()

    def get_service_name(self):
        return self.element_is_visible(Locators.SERVICE_NAME_ON_REQUEST).text

    def click_select_date_and_time_button(self):
        self.element_is_visible(Locators.SELECT_DATE_AND_TIME_BUTTON).click()

    def click_date_button(self):
        self.element_is_visible(Locators.FREE_DATE).click()

    def click_time_button(self):
        self.element_is_visible(Locators.FREE_TIME).click()

    def click_proceed_button(self):
        self.element_is_visible(Locators.PROCEED_TO_CONFIRMATION_BUTTON).click()

    def click_terms_and_conditions(self):
        self.element_is_visible(Locators.TERMS_AND_CONDITIONS_BUTTON).click()

    def click_confirm_button(self):
        self.element_is_visible(Locators.CONFIRM_BUTTON).click()

    def click_view_bookings_button(self):
        self.element_is_visible(Locators.VIEW_BOOKINGS_BUTTON).click()

    def get_service_name_final(self):
        return self.element_is_visible(Locators.SERVICE_NAME_FINAL).text

    def click_booking_card(self):
        self.element_is_visible(Locators.BOOKING_CARD).click()

    def click_cancel_button(self):
        self.element_is_visible(Locators.CANCEL_BUTTON).click()

    def click_cancel_button_modal(self):
        self.element_is_visible(Locators.CANCEL_BUTTON_MODAL).click()

