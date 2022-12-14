from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#login_form")
    USER_LOGIN = (By.CSS_SELECTOR, 'input[id="id_registration-email"]')
    USER_PASSWORD = (By.CSS_SELECTOR, 'input[id="id_registration-password1"]')
    VERIFICATION_USER_PASSWORD = (By.CSS_SELECTOR, 'input[id = "id_registration-password2"]')
    BUTTON_REGISTER = (By.CSS_SELECTOR, 'button[value="Register"]')


class ProductPageLocators:
    BUTTON_PUT_IN_BOX = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong ")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_GO_TO_BASKET = (By.CSS_SELECTOR, "div span.btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    MESSAGE_IN_BASKET = (By.CSS_SELECTOR, "div p:nth-child(1)")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, 'div .basket-items')


