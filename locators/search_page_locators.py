from selenium.webdriver.common.by import By


class SearchPageLocators:

    PERSON_LOCATION = (By.XPATH, '//div[@role="none"]/div[2]/span')
    SELECT_LOCATION_INPUT = (By.XPATH, '//div[@class="flex"]/div[2]/input')
    NUMBER_OF_RESULTS_HEADER = (By.XPATH, '//span[@class="text-orange"]')
