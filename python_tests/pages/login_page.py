from .base_page import BasePage
from .locators import LoginPageLocators
from enums.global_enums import *
from random_word import RandomWords

r = RandomWords()


class LoginPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

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

    def register_new_user(self):
        self.random_email()
        self.random_password()
        self.press_button_to_register()

    def random_email(self):
        email = r.get_random_word() + "@fakemail.org"
        user_login = self.browser.find_element(*LoginPageLocators.USER_LOGIN)
        user_login.send_keys(email)


    def random_password(self):
        password = r.get_random_word() + "123"
        user_password = self.browser.find_element(*LoginPageLocators.USER_PASSWORD)
        user_password.send_keys(password)
        user_password = self.browser.find_element(*LoginPageLocators.VERIFICATION_USER_PASSWORD)
        user_password.send_keys(password)

    def press_button_to_register(self):
        button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button.click()







