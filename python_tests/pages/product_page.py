from .base_page import BasePage
from .locators import ProductPageLocators
from enums.global_enums import *


class ProductPage(BasePage):
    def put_the_item_in_to_box_button(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_PUT_IN_BOX)
        button.click()

    def should_be_message_about_adding(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            GlobalProductPageMessage.PRODUCT_MISSING.value
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
            GlobalProductPageMessage.MESSAGE_ABOUT_ADDING_MISSING

        # получаем текст элементов для проверки
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text

        # Проверяем, что название товара присутствует в сообщении о добавлении
        assert product_name == message, GlobalProductPageMessage.WRONG_MESSAGE_ADDING.value

    def should_not_be_message_about_adding(self):
        assert self.is_element_not_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Success message is presented," \
                                                                                       "but should not be "

    def should_disappeared_message_about_adding(self):
        assert self.is_element_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Presented a success message" \
                                                                                       "but should have disappeared"

    def should_be_message_basket_total(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), \
            GlobalProductPageMessage.MESSAGE_BASKET_TOTAL_MISSING.value
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), \
            GlobalProductPageMessage.PRODUCT_PRICE_MISSING.value

        # Затем получаем текст элементов для проверки
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        # Проверяем, что цена товара присутствует в сообщении со стоимостью корзины
        assert product_price in message_basket_total, \
            GlobalProductPageMessage.WRONG_PRICE_IN_MESSAGE_BASKET_TOTAL.value
