import pytest

from configuration import *
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, LOGIN_URL)
    page.open()
    page.go_to_login_page()


@pytest.mark.skip
def test_should_be_login_link(browser):
    page = MainPage(browser, LOGIN_URL)
    page.open()
    page.should_be_login_link()


"""def test_verification_link(browser): # 1-ый вариант перехода между страницами
    page = MainPage(browser, LOGIN_URL)
    page.open()
    login_page = page.go_to_login_page() # вызываем метод, который инициализирует класс LoginPage
    login_page.should_be_login_page()"""


@pytest.mark.skip
def test_verification_link_2(browser):  # 2-ой вариант перехода между страницами
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)  # инициализируем LoginPage в теле теста
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, LOGIN_URL)
    page.open()
    page.should_be_link_to_the_basket()
    page.go_to_basket()
    page.should_not_be_items_in_basket()
    page.should_be_message_in_basket()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, CATALOGUE_URL)
    page.open()
    page.should_be_link_to_the_basket()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_message_in_basket()

