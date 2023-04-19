from selenium.webdriver.common.by import By


class ProfilePageLocators:
    CHANGE_NAME_BUTTON = (By.XPATH, '//div[@role="none"][2]/div[2]')
    FIRST_NAME_MODAL_INPUT = (By.XPATH, '//div[@style="max-width: 503px;"]/div[2]/div[1]//input')
    LAST_NAME_MODAL_INPUT = (By.XPATH, '//div[@style="max-width: 503px;"]/div[2]/div[2]//input')
    SAVE_BUTTON_MODAL = (By.XPATH, '//div[@class="opacity-100 transition"]/button')
    NAME_CHANGED_SUCCESSFULLY_MODAL = (By.XPATH, '//div[@style="max-width: 295px;"]/div/p')
    PROFILE_NAME = (By.XPATH, '//p[@class="text-black leading-7 text-20 font-bold  truncate "]')
    FULL_NAME = (By.XPATH, '//div[@role="none"][2]/div/div/div/div[2]//p[2]')
    PROFILE_PHOTO_INPUT = (By.XPATH, '//input[@type="file"]')