from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//div[@id='content_inner']//button[text()='Add to basket']")

    BOOK_NAME = (By.XPATH, "//div[@id='content_inner']//h1[contains(text(), 'The shellcoder')]")

    ADDED_TO_BASKET_MESSAGE = (By.XPATH, "//div[@id='messages']//div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]")

    BOOK_PRICE_PRODUCT_PAGE = (By.XPATH, "//p[@class='price_color']")

    BOOK_PRICE_ADDED_MESSAGE = (By.XPATH, "//div[@class='alertinner ']//p//strong")
