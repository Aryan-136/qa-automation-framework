"""
LoginPage - Page Object Model representing the Authentication Gateway.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://vault.aryancloud.internal/login"

    # Locators
    USERNAME_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "master-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_ALERT = (By.CLASS_NAME, "alert-danger")
    TWO_FACTOR_INPUT = (By.ID, "token-input")

    def load(self):
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_ALERT)

    def is_2fa_required(self):
        return self.is_visible(self.TWO_FACTOR_INPUT)