from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_on_add_to_basket_button(self):
        # self.should_be_add_basket_button()
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()


    def should_be_add_basket_button(self):
        assert self.is_element_is_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"

    def check_item_names_equal(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        item_added_message = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_MESSAGE).text
        print(item_name)
        print("=================")
        print(item_added_message)
        print("=================")
        assert item_name == item_added_message, "Item names aren't equal"

    def check_prices_equal(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        item_price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        print(item_price)
        print("=================")
        print(item_price_in_basket)
        print("=================")
        assert item_price == item_price_in_basket, "Prices aren't equal"

