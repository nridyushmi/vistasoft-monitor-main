from selenium.webdriver.common.by import By


class LoginPageLocators():
    """ Login page locators """
    LOGIN_LOGO = (By.CLASS_NAME, "heading-1 overflow-hidden")
    LOGIN_HEADER = (By.CLASS_NAME, "header flex justify-between items-end q-mb-xl")
    EMAIL_TEXTBOX = (By.ID, "email")
    PASSWORD_TEXTBOX = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MESSAGE_TEXT = (By.CLASS_NAME, "formulate-input-error")
    ERROR_PASSWORD_TEXT = (By.CLASS_NAME, "formulate-input-error" )
    LOGIN_BODY = (By.CLASS_NAME, "column flex overflow-hidden q-pa-sm-xl q-pa-xs-md full-width wrapper justify-center login-page")
    FORGET_PASSWORD_LINK = (By.CLASS_NAME, "link-layout__text")
    SIGN_UP_LINK = (By.CLASS_NAME, "link-layout__text")
    GOTO_WEBSITE_LINK = (By.CLASS_NAME, "justify-center items-center link-layout text-uppercase cursor-pointer")

class GeneralPageLocators():
    """ General Page Locators Shared between multiple pages """
    NAV_BAR_ITEMS = (By.CLASS_NAME, "_tid_hamburger-menu -mr-3 h-12 w-12 inline-flex items-center justify-center rounded-md text-primary-200 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-primary-600 cursor-pointer")

class Locators():
    """ Locators """
    LOGO = (By.ID, "duerr-dental-logo")
    HOMEPAGE_HEADER = (By.CLASS_NAME, "fixed flex items-center justify-between lg:hidden z-40 h-16 mt-safe inset-0 w-full bg-primary-800 border-b border-primary-900 px-4-safe py-1.5")
    USER_ACCOUNT = (By.CLASS_NAME, "flex w-full px-4 mb-2 pt-4 pb-safe")
    