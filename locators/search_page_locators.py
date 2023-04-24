from selenium.webdriver.common.by import By
from random import randint

class SearchPageLocators:

    PERSON_LOCATION = (By.XPATH, '//div[@role="none"]/div[2]/span')
    SELECT_LOCATION_INPUT = (By.XPATH, '//div[@class="flex"]/div[2]/input')
    SEARCH_FIRST_OPTION = (By.XPATH, '//div[@role="none"][1]/p')
    NUMBER_OF_RESULTS_HEADER = (By.XPATH, '//span[@class="text-orange"]')
    PERSON_CARD = (By.XPATH, f'(//a[@class="block"])[1]')
    NO_ITEMS_FOUND = (By.XPATH, '//p[text()="No Items Found!"]')
    BACK_BUTTON = (By.XPATH, '//div[@role="none"]')
    BOOK_BUTTON = (By.XPATH, '(//div[@class=" grid grid-cols-[400px_1fr] gap-[150px]"]//button)[1]')
    SERVICE_NAME = (By.XPATH, '(//div[@class=" grid grid-cols-[400px_1fr] gap-[150px]"]//button/parent::a/preceding-sibling::div/p)[1]')

