import time

from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators as Locators
from generator.generator import generated_data
from profile_images.valid.get_path import GetPath
from random import randint


class ProfilePage(BasePage):
    def click_change_name_button(self):
        self.element_is_visible(Locators.CHANGE_NAME_BUTTON).click()

    def fill_first_name_field(self):
        profile_data = next(generated_data())
        first_name = profile_data.first_name
        self.element_is_visible(Locators.FIRST_NAME_MODAL_INPUT).send_keys(first_name)
        return first_name

    def fill_last_name_field(self):
        profile_data = next(generated_data())
        last_name = profile_data.last_name
        self.element_is_visible(Locators.LAST_NAME_MODAL_INPUT).send_keys(last_name)
        return last_name

    def click_save_button(self):
        self.element_is_visible(Locators.SAVE_BUTTON_MODAL).click()

    def get_profile_name(self):
        text = self.element_is_visible(Locators.PROFILE_NAME).text
        return text

    def get_full_name(self):
        text = self.element_is_visible(Locators.FULL_NAME).text
        return text

    def upload_profile_photo(self):
        img_formats = ['jpg', 'png']
        path = str(GetPath.path) + fr'\{randint(1, 5)}.{img_formats[randint(0, 1)]}'
        self.element_is_present(Locators.PROFILE_PHOTO_INPUT).send_keys(path)
        time.sleep(10)

    def click_change_email_button(self):
        self.element_is_visible(Locators.CHANGE_EMAIL_BUTTON).click()

    def fill_password_field(self, password):
        self.element_is_visible(Locators.PASSWORD_MODAL_INPUT).send_keys(password)

    def new_email(self):
        profile_data = next(generated_data())
        email = profile_data.email
        return email

    def set_new_email(self, email):
        self.element_is_visible(Locators.NEW_EMAIL_MODAL_INPUT).send_keys(email)

    def log_out(self):
        self.element_is_visible(Locators.ACCOUNT_BUTTON).click()
        self.element_is_visible(Locators.LOG_OUT_BUTTON).click()

    def get_new_email(self):
        return self.element_is_visible(Locators.EMAIL).text

    def email_changed_modal_displayed(self):
        return self.element_is_visible(Locators.EMAIL_CHANGED_MODAL).is_displayed()