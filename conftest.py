"""
PyTest Configuration & Reusable Browser Fixtures
Supports Headless Chrome, Cross-Browser Matrix, and HTML Reporting.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")
    parser.addoption("--headless", action="store_true", default=True, help="Run browser in headless mode")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    is_headless = request.config.getoption("--headless")

    if browser_name.lower() == "firefox":
        options = FirefoxOptions()
        if is_headless:
            options.add_argument("--headless")
        driver_instance = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        if is_headless:
            options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        driver_instance = webdriver.Chrome(options=options)

    driver_instance.implicitly_wait(5)
    yield driver_instance
    driver_instance.quit()