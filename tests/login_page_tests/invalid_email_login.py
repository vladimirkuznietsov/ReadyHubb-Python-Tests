import time

from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestInvalidEmailLogin:

    def test_invalid_email_login(self, driver):
        home_page = HomePage(driver, 'https://readyhubb.com/')
        login_page = LoginPage(driver, 'https://readyhubb.com/')
        home_page.open()
        home_page.click_sign_in_button()
        login_page.fill_email_field('test@email123')
        login_page.fill_password_field('Automation@test2023')
        login_page.click_sign_in_button()
        time.sleep(0.5)
        actual_border_color = login_page.get_email_input_border_color()
        actual_alert_text = login_page.get_invalid_email_message()
        assert actual_border_color == '#f36a46'
        assert actual_alert_text == 'Enter valid email'

