from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators
import time

class BasketPage(BasePage):

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket has a item in it, but should not"

    def should_be_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "Basket is empty message is not present"