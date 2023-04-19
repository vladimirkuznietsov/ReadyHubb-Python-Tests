from selenium.webdriver.support.color import Color

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators as Locators


class LoginPage(BasePage):

    def sign_in_button_is_enabled(self):
        all_styles = self.element_is_present(Locators.SIGN_IN_BUTTON).get_attribute('class')
        if 'opacity-40' in all_styles:
            return False
        else:
            return True

    def fill_email_field(self, email):
        self.element_is_visible(Locators.EMAIL_INPUT_FIELD).send_keys(email)

    def fill_password_field(self, password):
        self.element_is_visible(Locators.PASSWORD_INPUT_FIELD).send_keys(password)

    def click_sign_in_button(self):
        self.element_is_visible(Locators.SIGN_IN_BUTTON).click()

    def get_email_input_border_color(self):
        color = Color.from_string(
            self.element_is_visible(Locators.EMAIL_INPUT_FIELD).value_of_css_property('border-color')).hex
        return color

    def get_password_input_border_color(self):
        color = Color.from_string(
            self.element_is_visible(Locators.PASSWORD_INPUT_FIELD).value_of_css_property('border-color')).hex
        return color

    def get_email_pass_messages(self):
        texts = [i.text for i in self.elements_are_visible(Locators.INVALID_EMAIL_PASS_MESSAGE)]
        return texts

    def login(self, email, password):
        self.fill_email_field(email)
        self.fill_password_field(password)
        self.click_sign_in_button()
