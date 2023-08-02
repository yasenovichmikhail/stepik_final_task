from .base_page import BasePage
from .locators import LoginPageLocators, RegisterPageLocators, TestData, ProductPageLocators
from .locators import MainPageLocators

from .main_page import MainPage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current = self.get_current_url()
        assert 'login' in current, "Current url doesn't contain login"

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_book_link(self):
        self.click(*ProductPageLocators.BOOK_LINK)

    def register_new_user(self):
        input_email = self.browser.find_element(*RegisterPageLocators.EMAIL_ADDRESS_FIELD)
        input_email.send_keys(TestData.email)
        input_password = self.browser.find_element(*RegisterPageLocators.PASSWORD_FIELD)
        input_password.send_keys(TestData.password)
        confirm_password = self.browser.find_element(*RegisterPageLocators.CONFIRM_PASSWORD_FIELD)
        confirm_password.send_keys(TestData.password)
        register_button = self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON)
        register_button.click()
