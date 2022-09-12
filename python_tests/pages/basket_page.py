from .base_page import BasePage
from .locators import BasketPageLocators
from enums.global_enums import GlobalBasketPageMessage


class BasketPage(BasePage):
    def should_be_message_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_IN_BASKET), \
            GlobalBasketPageMessage.MESSAGE_IN_BASKET_MISSING.value

        message_in_basket = self.browser.find_element(*BasketPageLocators.MESSAGE_IN_BASKET).text
        assert "basket is empty" in message_in_basket, GlobalBasketPageMessage.WRONG_MESSAGE_IN_BASKET.value

    def should_not_be_items_in_basket(self):
        assert self.is_element_not_present(*BasketPageLocators.ITEMS_IN_BASKET), "The basket isn't empty but" \
                                                                                 " should be"
