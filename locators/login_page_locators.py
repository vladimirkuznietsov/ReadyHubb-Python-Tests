from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT_FIELD = (By.XPATH, '//input[@type="text"]')
    PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@type="password"]')
    SIGN_IN_BUTTON = (By.XPATH, '//div[@id="app_layout"]/div/div[2]/form/button[1]')
    INVALID_EMAIL_MESSAGE = (By.XPATH, '//div[@id="app_layout"]/div/div[2]/form/div/div/span')
    INVALID_EMAIL_PASS_MESSAGE = (By.XPATH, '//span[text()="Wrong login or password"]')
