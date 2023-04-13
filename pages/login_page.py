from selenium.webdriver.support.color import Color

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators as Locators


class LoginPage(BasePage):

    def is_sign_in_button_enabled(self):
        state = self.element_is_visible(Locators.SIGN_IN_BUTTON)
        return state.is_enabled()

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
