from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_basket_item(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "Basket item is presented, but should not be"

    def should_be_text_empty_basket(self):
        expected_text = "Your basket is empty"
        actual_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_ITEM).text
        assert expected_text in actual_text, \
            "Text Your basket is empty is not appeared"
