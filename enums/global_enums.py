from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not as expected"
    WRONG_ELEMENT_COUNT = "Number of element is not equal to expected"
    LINK_MISSING = "Link is not presented"
    WRONG_URL_NAME = "The browser's current url name doesn't match the expected"
    BUTTON_MISSING = "Button is not presented"


class GlobalFormMessages(Enum):
    LINK_FORM_MISSING = "Login form is not presented"
    REGISTER_FORM_MISSING = "Register form is not presented"

class GlobalUserLoginMessages(Enum):
    REGISTER_FORM_LOGIN_MISSING = "Login link in register form is not presented"
    REGISTER_FORM_PASSWORD_MISSING = "Password link in register form is not presented"


class GlobalProductPageMessage(Enum):
    PRODUCT_MISSING = "Product is not presented"
    MESSAGE_ABOUT_ADDING_MISSING = "Message about adding is not presented"
    WRONG_MESSAGE_ADDING = "Product name not provided in final cart message"

    MESSAGE_BASKET_TOTAL_MISSING = "Message basket total is not presented"
    PRODUCT_PRICE_MISSING = "Product price is not presented"
    WRONG_PRICE_IN_MESSAGE_BASKET_TOTAL = "Total price of the basket isn't right"


class GlobalBasketPageMessage(Enum):
    MESSAGE_IN_BASKET_MISSING = "Message about items in basket is not presented"
    WRONG_MESSAGE_IN_BASKET = "Wrong message in basket, it isn't empty"

