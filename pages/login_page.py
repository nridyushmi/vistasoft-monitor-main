import pages.homepage
from utils.base_page import BasePage
from resources.page_locators import LoginPageLocators
from resources.page_locators import Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    @property
    def login_btn_el(self):
        return self.driver.find_element(*LoginPageLocators.LOGIN_BTN)

    def enter_username(self, username):
        username_textbox = self.driver.find_element(*LoginPageLocators.EMAIL_TEXTBOX)
        username_textbox.clear()
        username_textbox.send_keys(username, Keys.ENTER)

    def enter_password(self, password):
        pw_textbox_el = self.driver.find_element(*LoginPageLocators.PASSWORD_TEXTBOX)
        pw_textbox_el.clear()
        pw_textbox_el.send_keys(password, Keys.ENTER)

    def click_login(self):
        click_login = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BTN))
        click_login.click()
        return pages.homepage.HomePage(self.driver)

    def get_error_message(self):
        error_message = self.driver.find_element(*LoginPageLocators.ERROR_MESSAGE_TEXT).text
        return error_message.replace("error\n", "")

    def homepage_url(self):
        WebDriverWait(self.driver, 160).until(EC.element_to_be_clickable(*Locators.USER_ACCOUNT))
        current_url = self.driver.current_url
        return current_url