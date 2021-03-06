from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def click_on_add_to_basket_button(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_add_basket_button(self):
        assert self.is_element_is_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"

    def check_item_names_equal(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        item_added_message = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_MESSAGE).text
        print(item_name)
        print(item_added_message)
        assert item_name == item_added_message, "Item names aren't equal"

    def check_prices_equal(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        item_price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        print(item_price)
        print(item_price_in_basket)
        assert item_price == item_price_in_basket, "Prices aren't equal"

    def should_not_presented_succeed_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_ADDED_MESSAGE), "Item is presented"

    def should_disappeared_success_message(self):
        assert self.is_element_is_present(*ProductPageLocators.ITEM_ADDED_MESSAGE), "Item isn't presented"
        assert self.is_disappeared(*ProductPageLocators.ITEM_ADDED_MESSAGE), "Success message still presented"
