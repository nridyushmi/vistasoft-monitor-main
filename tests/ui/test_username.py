import pytest
from requests import request
from pages.homepage import HomePage
from utils.base_test import BaseTest
from pages.login_page import LoginPage

class TestUser(BaseTest):

    def test_valid_username(self, user):
        login_page = LoginPage(self.driver)
        login_page.enter_username(user.username)
        login_page.enter_password(user.password)
        login_page.click_login()

    def test_invalid_login_empty_username(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username(" ")
        login_page.click_login()
        assert login_page.get_error_message() == "Email is required."