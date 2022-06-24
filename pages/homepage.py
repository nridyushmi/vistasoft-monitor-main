from selenium.webdriver.support.wait import WebDriverWait
from resources.page_locators import Locators, GeneralPageLocators, LoginPageLocators
from utils.base_page import BasePage

class HomePage(BasePage):

    @property
    def profile_button (self, username):
        username_textbox = self.driver.find_element(*LoginPageLocators.EMAIL_TEXTBOX)
        username_textbox.clear()
        username_textbox.send_keys(username, Keys.ENTER)

