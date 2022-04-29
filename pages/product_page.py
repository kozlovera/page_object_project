from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_to_basket_button.click()
        #self.solve_quiz_and_get_code()
        #time.sleep(3)
        #self.should_be_product_added_message()
        #self.should_be_basket_total_message()

    def should_be_product_added_message(self):

        book_added_message = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_MESSAGE)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        assert book_name.text == product_name.text, "Confirmation message does not include name of product"

    def should_be_basket_total_message(self):
        basket_total_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE)
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        assert price.text in basket_total_message.text, "Basket price does not equal price of product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), "Success message is not disappeared, but should  be"


