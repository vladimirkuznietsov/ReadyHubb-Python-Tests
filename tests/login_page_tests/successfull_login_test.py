from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestSuccessfulLogin:

    def test_successful_login(self, driver):
        home_page = HomePage(driver, 'https://readyhubb.com/')
        login_page = LoginPage(driver, 'https://readyhubb.com/')

        home_page.open()
        home_page.click_sign_in_button()
        login_page.fill_email_field()
        login_page.fill_password_field()
        login_page.click_sign_in_button()
        actual_options = home_page.click_account_button()
        assert home_page.expected_options == actual_options