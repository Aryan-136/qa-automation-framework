"""
LoginPage - Page Object Model representing the Authentication Portal.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    PATH = "/login"

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_ALERT = (By.ID, "flash")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")

    def __init__(self, driver, base_url="https://the-internet.herokuapp.com", timeout=10):
        super().__init__(driver, timeout)
        self.url = f"{base_url.rstrip('/')}{self.PATH}"

    def load(self):
        self.open(self.url)
        return self

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def get_flash_message(self):
        return self.get_text(self.FLASH_ALERT)

    def is_logged_in(self):
        return self.is_visible(self.LOGOUT_BUTTON, timeout=3)

    def logout(self):
        self.click(self.LOGOUT_BUTTON)
        return self
