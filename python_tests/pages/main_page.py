from .base_page import BasePage
from enums.global_enums import GlobalErrorMessages
from .locators import MainPageLocators


# from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        def __init__(self, *args, **kwargs):
            super(MainPage, self).__init__(*args, **kwargs)
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        # * означает,что мы передаем пару и этот кортеж надо распаковать
        login_link.click()

        # return LoginPage(browser=self.browser, url=self.browser.current_url)
        # возвращаем браузер и url для класса LoginPage, таким образом инициализируем его

        # alert = self.browser.switch_to.alert есди появилось всплывающее окно
        # alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), GlobalErrorMessages.LINK_MISSING.value


