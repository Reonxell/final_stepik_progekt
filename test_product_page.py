from pages.product_page import ProductPage
from pages.locators import ProductPageLocators


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.BASKET_URL)
    page.open()
    page.show_add_basket()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.show_alert_add_basket()
    page.name_products_in_basket()
    page.prise_products_in_basket()

