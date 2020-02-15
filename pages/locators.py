from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    ITEM_ADDED_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main>h1")



