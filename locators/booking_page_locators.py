from selenium.webdriver.common.by import By


class BookingPageLocators:
    NO_BOOKINGS_HEADER = (By.XPATH, '(//section//p)[1]')
    SEARCH_NEARBY_BUTTON = (By.XPATH, '//span[text()="Search nearby"]//parent::div/parent::button')
    SERVICE_NAME_ON_REQUEST = (By.XPATH, '//span[text()="Choose a service"]/parent::div/following-sibling::div//p')
    SELECT_DATE_AND_TIME_BUTTON = (By.XPATH, '//span[text()="Select date and time"]/parent::div/parent::button')
    FREE_DATE = (By.XPATH, '//p[@class="text-black leading-[22px] text-16 font-normal block  flex items-center justify-center transition rounded-[12px] w-full h-full cursor-pointer false hover:bg-lightGray text-black   "]')
    FREE_TIME = (By.XPATH, '//div[@id="headlessui-portal-root"]//div[1]//div[2]//div[1]//div[5]/div/div[1]')
    PROCEED_TO_CONFIRMATION_BUTTON = (By.XPATH, '//span[text()="Proceed to confirmation"]/parent::div/parent::button')
    TERMS_AND_CONDITIONS_BUTTON = (By.XPATH, '//div[@id="booking_agreement"]/div/div')
    CONFIRM_BUTTON = (By.XPATH, '//span[text()="Confirm"]/parent::div/parent::button')
    VIEW_BOOKINGS_BUTTON = (By.XPATH, '//span[text()="View my Bookings"]/parent::div/parent::button')
    SERVICE_NAME_FINAL = (By.XPATH, '//section/div/div/div[2]/div/div/div[2]//p[1]')
    BOOKING_CARD = (By.XPATH, '(//div[@class="cursor-pointer"])[1]')
    CANCEL_BUTTON = (By.XPATH, '//span[text()="Cancel"]/parent::div')
    CANCEL_BUTTON_MODAL = (By.XPATH, '//span[text()="Are you sure you want to cancel booking?"]/parent::div//button[1]')