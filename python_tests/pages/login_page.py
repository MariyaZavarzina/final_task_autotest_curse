from .base_page import BasePage
from .locators import LoginPageLocators
from enums.global_enums import *


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_substring()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_substring(self):
        assert "login" in self.browser.current_url, GlobalErrorMessages.WRONG_URL_NAME.value

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), GlobalFormMessages.LINK_FORM_MISSING.value

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), GlobalFormMessages.REGISTER_FORM_MISSING.value
