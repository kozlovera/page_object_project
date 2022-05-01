from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators




class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        cur_url = self.browser.current_url
        # реализуйте проверку на корректный url адрес
        assert 'login/' in cur_url, "URL does not contain login-substring"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_field.send_keys(password)
        password_confirm_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
        password_confirm_field.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators. REGISTER_BUTTON)
        button.click()


