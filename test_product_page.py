import pytest
from selenium import webdriver
from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,link)
    page.open()
    page.should_be_add_basket_button()
    page.click_on_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.check_item_names_equal()
    page.check_prices_equal()
