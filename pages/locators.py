from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET_BUTTON = (By.XPATH, "//a[@class='btn btn-default'][@href='/en-gb/basket/']")


class BasketPageLocators:
    BASKET_ITEM = (By.XPATH, "//div[@class='basket-items']")
    BASKET_EMPTY_ITEM = (By.XPATH, "//div[@id='content_inner']")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//div[@id='content_inner']//button[text()='Add to basket']")
    BOOK_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']//h1")
    ADDED_NAME_BASKET_MESSAGE = (By.XPATH, "//div[@id='messages']//div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]//strong")
    BOOK_PRICE_PRODUCT_PAGE = (By.XPATH, "//p[@class='price_color']")
    BOOK_PRICE_ADDED_MESSAGE = (By.XPATH, "//div[@class='alertinner ']//p//strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']//div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]")