from selenium.webdriver.common.by import By


class ProfilePageLocators:
    CHANGE_NAME_BUTTON = (By.XPATH, '//div[@role="none"][2]/div[2]')
    FIRST_NAME_MODAL_INPUT = (By.XPATH, '//div[@style="max-width: 503px;"]/div[2]/div[1]//input')
    LAST_NAME_MODAL_INPUT = (By.XPATH, '//div[@style="max-width: 503px;"]/div[2]/div[2]//input')
    SAVE_BUTTON_MODAL = (By.XPATH, '//span[text()="Save"]/parent::div/parent::button')
    NAME_CHANGED_SUCCESSFULLY_MODAL = (By.XPATH, '//div[@style="max-width: 295px;"]/div/p')
    PROFILE_NAME = (By.XPATH, '//p[@class="text-black leading-7 text-20 font-bold  truncate "]')
    FULL_NAME = (By.XPATH, '//div[@class="grid desktop:grid-cols-2 gap-4 mt-4"]/div[2]/div[1]/p[2]')
    PROFILE_PHOTO_INPUT = (By.XPATH, '//input[@type="file"]')
    CHANGE_EMAIL_BUTTON = (By.XPATH, '//p[text()="Email"]/parent::div/parent::div/div[2]')
    PASSWORD_MODAL_INPUT = (By.XPATH, '//input[@type="password"]')
    NEW_EMAIL_MODAL_INPUT = (By.XPATH, '//input[@type="text"]')
    EMAIL = (By.XPATH, '//p[text()="Email"]/following-sibling::p')
    ACCOUNT_BUTTON = (By.XPATH, '//header/div[2]/div[2]/div')
    LOG_OUT_BUTTON = (By.XPATH, '//div[@data-placement="bottom-end"]/div/div')
    EMAIL_CHANGED_MODAL = (By.XPATH, '//p[text()="Your email has been changed successfully"]')