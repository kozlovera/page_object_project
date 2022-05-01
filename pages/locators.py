from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#register_form input#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#register_form input#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#register_form input#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "form#add_to_basket_form button.btn")
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) div.alertinner")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.alert:nth-child(1) div.alertinner strong")
    BOOK_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(3) div.alertinner")
    PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div#content_inner")



