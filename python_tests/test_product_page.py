import pytest
from configuration import *
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.parametrize('offer', ["offer0", "offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={offer}"
    page = ProductPage(browser, link)
    page.open()
    page.put_the_item_in_to_box_button()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, CATALOGUE_URL_SEC_ITEM)
    page.open()
    page.put_the_item_in_to_box_button()
    page.solve_quiz_and_get_code()
    page.should_not_be_message_about_adding()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, CATALOGUE_URL_SEC_ITEM)
    page.open()
    page.should_not_be_message_about_adding()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, CATALOGUE_URL_SEC_ITEM)
    page.open()
    page.put_the_item_in_to_box_button()
    page.solve_quiz_and_get_code()
    page.should_disappeared_message_about_adding()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, CATALOGUE_URL)
    page.open()
    page.should_be_link_to_the_basket()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_message_in_basket()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user()
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, CATALOGUE_URL)
        page.open()
        page.put_the_item_in_to_box_button()
        page.solve_quiz_and_get_code()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, CATALOGUE_URL)
        page.open()
        page.should_not_be_message_about_adding()

