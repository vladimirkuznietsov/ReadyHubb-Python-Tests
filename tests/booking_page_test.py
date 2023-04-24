import time

from data.data import Data
from pages.booking_page import BookingPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage


class TestBookingPage:

    def test_book_service(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        search_page = SearchPage(driver)
        booking_page = BookingPage(driver)

        home_page.click_sign_in_button()
        assert not login_page.sign_in_button_is_enabled()
        login_page.fill_email_field(Data.email)
        assert not login_page.sign_in_button_is_enabled()
        login_page.fill_password_field(Data.password)
        login_page.click_sign_in_button()
        home_page.click_account_button()
        home_page.click_account_option(0)
        time.sleep(2)
        assert booking_page.get_no_bookings_header_text() == Data.no_bookings_message
        booking_page.click_search_button()
        time.sleep(3)
        search_page.fill_search_field(Data.location)
        search_page.select_first_location_option()
        search_page.click_person_card()
        service_name = search_page.get_service_name()
        search_page.click_book_button()
        assert service_name == booking_page.get_service_name()
        booking_page.click_select_date_and_time_button()
        booking_page.click_date_button()
        booking_page.click_time_button()
        booking_page.click_proceed_button()
        booking_page.click_terms_and_conditions()
        booking_page.click_confirm_button()
        booking_page.click_view_bookings_button()
        assert service_name == booking_page.get_service_name_final()
        booking_page.click_booking_card()
        booking_page.click_cancel_button()
        booking_page.click_cancel_button_modal()
        driver.refresh()
        assert Data.no_bookings_message == booking_page.get_no_bookings_header_text()
