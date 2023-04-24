import time
import unittest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from data.data import Data
from pages.profile_page import ProfilePage
from profile_images.valid.get_path import GetPath


class TestUserData():
    first_name = None
    last_name = None

    def test_change_name(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        
        home_page.click_sign_in_button()
        login_page.login(Data.email, Data.password)
        home_page.click_account_button()
        home_page.click_account_option(2)
        profile_page.click_change_name_button()
        first_name = profile_page.fill_first_name_field()
        last_name = profile_page.fill_last_name_field()
        profile_page.click_save_button()
        time.sleep(1)
        driver.refresh()

        assert profile_page.get_profile_name() == first_name + ' ' + last_name
        assert profile_page.get_full_name() == first_name + ' ' + last_name

    def test_change_profile_photo(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        home_page.click_sign_in_button()
        login_page.login(Data.email, Data.password)
        home_page.click_account_button()
        home_page.click_account_option(2)
        profile_page.upload_profile_photo()

    def test_change_email(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        home_page.click_sign_in_button()
        login_page.login(Data.email, Data.password)
        home_page.click_account_button()
        home_page.click_account_option(2)
        profile_page.click_change_email_button()
        profile_page.fill_password_field(Data.password)
        new_email = profile_page.new_email()
        profile_page.set_new_email(new_email)
        profile_page.click_save_button()
        assert profile_page.email_changed_modal_displayed()
        driver.refresh()
        assert profile_page.get_new_email() == new_email
        profile_page.log_out()
        home_page.click_sign_in_button()
        login_page.login(new_email, Data.password)
        home_page.click_account_button()
        home_page.click_account_option(2)
        profile_page.click_change_email_button()
        profile_page.fill_password_field(Data.password)
        profile_page.set_new_email(Data.email)
        profile_page.click_save_button()
        assert profile_page.email_changed_modal_displayed()
        driver.refresh()
        assert profile_page.get_new_email() == Data.email