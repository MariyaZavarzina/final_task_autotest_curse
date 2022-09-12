import time

import pytest
from configuration import CATALOGUE_URL_SEC_ITEM
from .pages.product_page import ProductPage


@pytest.mark.parametrize('offer', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                                   pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
@pytest.mark.skip
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


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
