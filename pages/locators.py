from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    BASKET_URL = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    ADD_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_PRODUCTS = (By.CSS_SELECTOR, '.product_main h1')
    NAME_PRODUCTS_ADD_BASKET = (By.CSS_SELECTOR, '.alertinner strong')
    PRICE_PRODUCTS = (By.CSS_SELECTOR, '.product_main p.price_color')
    PRICE_PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, '.alertinner p strong')
    ALERT_ADD_TO_BASKET = (By.ID, 'messages')


