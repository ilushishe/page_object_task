from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        registration_login_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_LOGIN_INPUT_FIELD)
        registration_login_field.send_keys(email)
        registration_password_field1 = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD_INPUT_FIELD_FIRST)
        registration_password_field1.send_keys(password)
        registration_password_field2 = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD_INPUT_FIELD_SECOND)
        registration_password_field2.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "url doesn't contain 'login'"

    def should_be_login_form(self):
        assert self.is_element_is_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_is_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
