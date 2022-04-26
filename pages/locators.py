from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "form#add_to_basket_form button.btn")
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) div.alertinner")
    BOOK_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(3) div.alertinner")
    PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")