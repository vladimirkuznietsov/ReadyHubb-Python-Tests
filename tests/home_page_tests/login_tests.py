import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from data.data import Data
from locators.login_page_locators import LoginPageLocators as Locators


class TestSuccessfulLogin:

    def test_successful_login(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        home_page.click_sign_in_button()
        assert not login_page.is_sign_in_button_enabled()
        login_page.fill_email_field(Data.email)
        login_page.fill_password_field(Data.password)
        login_page.click_sign_in_button()
        actual_options = home_page.click_account_button()

        assert home_page.expected_account_dropdown_options == actual_options

    def test_invalid_email_login(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        home_page.click_sign_in_button()
        assert not login_page.is_sign_in_button_enabled()
        login_page.fill_email_field(Data.invalid_email)
        login_page.fill_password_field(Data.password)
        login_page.click_sign_in_button()
        time.sleep(0.5)
        actual_messages = login_page.get_email_pass_messages()
        actual_colors = [login_page.get_email_input_border_color(), login_page.get_password_input_border_color()]

        for i in actual_messages:
            assert i == Data.invalid_login_message

        for i in actual_colors:
            assert i == Data.border_color_invalid_login

    def test_invalid_password(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        home_page.click_sign_in_button()
        assert not login_page.is_sign_in_button_enabled()
        login_page.fill_email_field(Data.email)
        login_page.fill_password_field(Data.invalid_password)
        login_page.click_sign_in_button()
        time.sleep(0.5)
        actual_messages = login_page.get_email_pass_messages()
        actual_colors = [login_page.get_email_input_border_color(), login_page.get_password_input_border_color()]

        for i in actual_messages:
            assert i == Data.invalid_login_message

        for i in actual_colors:
            assert i == Data.border_color_invalid_login
