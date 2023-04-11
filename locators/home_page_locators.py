from selenium.webdriver.common.by import By


class HomePageLocators:
    SIGN_IN_BUTTON = (By.XPATH, '//header/div[2]/button[1]')
    ACCOUNT_BUTTON = (By.XPATH, '//header/div[2]/div[2]')
    ACCOUNT_OPTIONS = (By.XPATH, '//div[@id="tippy-2"]/div/a')
    LOGOUT_BUTTON = (By.XPATH, '//div[@id="tippy-2"]/div/div')