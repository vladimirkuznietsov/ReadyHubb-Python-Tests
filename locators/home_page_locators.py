from selenium.webdriver.common.by import By


class HomePageLocators:
    SIGN_IN_BUTTON = (By.XPATH, '//header/div[2]/div/button[1]')
    ACCOUNT_BUTTON = (By.XPATH, '//header/div[2]/div[2]/div')
    ACCOUNT_OPTIONS = (By.XPATH, '//div[@data-placement="bottom-end"]/a')
    LOGOUT_BUTTON = (By.XPATH, '//p[text()="Log out"]/parent::div')
    SELECT_LOCATION_INPUT = (By.XPATH, '//div[@class="flex"]/div[2]/input')
    SEARCH_FIRST_OPTION = (By.XPATH, '//div[@role="none"][1]/p')