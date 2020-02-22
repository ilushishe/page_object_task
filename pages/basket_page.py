from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_CONTAINER), "Item is presented"

    def should_be_basket_is_empy_message(self):
        assert self.is_element_is_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), "Message isn't presented"
