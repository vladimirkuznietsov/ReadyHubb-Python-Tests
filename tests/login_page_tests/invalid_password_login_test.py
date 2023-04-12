import time

from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestInvalidPasswordLogin:

    def test_invalid_password(self, driver):
        home_page = HomePage(driver, 'https://readyhubb.com/')
        login_page = LoginPage(driver, 'https://readyhubb.com/')

        home_page.open()
        home_page.click_sign_in_button()
        login_page.fill_email_field('vladimir.kuznetsov@white-test.com')
        login_page.fill_password_field('123123123')
        login_page.click_sign_in_button()
        time.sleep(0.5)
        actual_messages = login_page.get_email_pass_messages()
        acual_colors = [login_page.get_email_input_border_color(), login_page.get_password_input_border_color()]
        for i in actual_messages:
            assert i == 'Wrong login or password'

        for i in acual_colors:
            assert i == '#f36a46'
