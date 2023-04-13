from selenium.webdriver.common.by import By


class HomePageLocators:
    SIGN_IN_BUTTON = (By.XPATH, '//header/div[2]/button[1]')
    ACCOUNT_BUTTON = (By.XPATH, '//header/div[2]/div[2]')
    ACCOUNT_OPTIONS = (By.XPATH, '//div[@id="tippy-2"]/div/a')
    LOGOUT_BUTTON = (By.XPATH, '//div[@id="tippy-2"]/div/div')
    SELECT_LOCATION_INPUT = (By.XPATH, '//div[@class="flex"]/div[2]/input')
    SEARCH_FIRST_OPTION = (By.XPATH, '//div[@role="none"][1]/p')