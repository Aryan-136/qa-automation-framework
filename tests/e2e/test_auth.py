"""
End-to-End Authentication Test Suite.
Validates login, credential rejection, and session teardown using the LoginPage POM.
"""
import pytest
from pages.login_page import LoginPage


@pytest.mark.e2e
class TestAuthentication:

    @pytest.mark.smoke
    def test_successful_login(self, driver, base_url):
        """Verify successful authentication with valid credentials."""
        login_page = LoginPage(driver, base_url=base_url).load()
        login_page.login("tomsmith", "SuperSecretPassword!")

        assert login_page.is_logged_in(), "Expected user to be authenticated with logout option visible."
        assert "You logged into a secure area!" in login_page.get_flash_message()

    @pytest.mark.regression
    def test_invalid_credentials_shows_error(self, driver, base_url):
        """Verify authentication failure and error alert on invalid credentials."""
        login_page = LoginPage(driver, base_url=base_url).load()
        login_page.login("invalid_user", "invalid_password")

        assert not login_page.is_logged_in(), "User should not be logged in with invalid credentials."
        assert "Your username is invalid!" in login_page.get_flash_message()

    @pytest.mark.regression
    def test_logout_flow(self, driver, base_url):
        """Verify session invalidation and redirect upon logout."""
        login_page = LoginPage(driver, base_url=base_url).load()
        login_page.login("tomsmith", "SuperSecretPassword!")
        login_page.logout()

        assert not login_page.is_logged_in(), "User should be logged out."
        assert "You logged out of the secure area!" in login_page.get_flash_message()
