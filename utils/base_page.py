from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """ Base Page class to be inherited by all pages
    Contains methods general to all pages """

    INITIAL_LOAD_WAIT = 30  # seconds
    ELEMENT_WAIT = 40  # seconds

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(self.INITIAL_LOAD_WAIT)

    #def get_page_header(self):
        #header = self.driver.find_element(By.CSS_SELECTOR, "h1[data-test-id*=page-header]")
        #return BaseElement(header)

    def get_element_wait_for_clickable(self, locator):
        print(locator)
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))
    
    def get_element_wait_for_visibility_located(self, locator):
        print(locator)
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))