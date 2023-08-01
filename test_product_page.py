import pytest
from .pages.product_page import ProductPage
import time


@pytest.mark.parametrize("promo_offer", ["promo=offer0", "promo=offer1", "promo=offer2", "promo=offer3", \
                                         "promo=offer4", "promo=offer5", "promo=offer6", "promo=offer7", \
                                         "promo=offer8", "promo=offer9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_name_added_book()
    page.check_price_added_book()
    time.sleep(5)
