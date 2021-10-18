from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def name_products_in_basket(self):
        name_products = self.browser.find_element(*ProductPageLocators.NAME_PRODUCTS).text
        name_products_in_basket = self.browser.find_element(*ProductPageLocators.NAME_PRODUCTS_ADD_BASKET).text
        assert name_products == name_products_in_basket, f'Имена не совпадают, ожидали {name_products}' \
                                                         f', а получили {name_products_in_basket}'

    def prise_products_in_basket(self):
        prise_products = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCTS).text
        prise_products_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCTS_IN_BASKET).text
        assert prise_products == prise_products_in_basket, f'Цены не совпадают, ожидали {prise_products}, ' \
                                                           f'а получили {prise_products_in_basket}'

    def show_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET), 'Нет страницы добаления в корзину'

    def show_alert_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_ADD_TO_BASKET), 'Нет поп-апа добавления в корзину'

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BASKET).click()
