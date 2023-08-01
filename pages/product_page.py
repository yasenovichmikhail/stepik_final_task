import pytest
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def check_name_added_book(self):
        expected_book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        added_name_basket_message = self.browser.find_element(*ProductPageLocators.ADDED_NAME_BASKET_MESSAGE).text
        assert expected_book_name == added_name_basket_message, "Book name doesn't match"

    def check_price_added_book(self):
        expected_book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_PRODUCT_PAGE).text
        actual_book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ADDED_MESSAGE).text
        assert expected_book_price == actual_book_price, "Price of the book doesn't match"

