from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "[href*='/basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_LOGIN_INPUT_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_INPUT_FIELD_FIRST = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_INPUT_FIELD_SECOND = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    ITEM_ADDED_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main>h1")


class BasketPageLocators():
    BASKET_ITEMS_CONTAINER = (By.CSS_SELECTOR, ".basket-items")
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
