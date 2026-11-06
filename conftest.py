"""
PyTest Configuration & Reusable Browser Fixtures.
Cross-browser factory (Chrome & Firefox), headless-by-default, and failure screenshots.
"""
import os
from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox"], help="Browser choice")
    parser.addoption("--headed", action="store_true", default=False, help="Run browser in visible (headed) mode")
    parser.addoption("--base-url", action="store", default=os.getenv("BASE_URL", "https://the-internet.herokuapp.com"), help="Base URL for tests")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url").rstrip("/")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser").lower()
    headless = not request.config.getoption("--headed")

    if browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        driver_instance = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        driver_instance = webdriver.Chrome(options=options)

    # Attach driver to test item for screenshot hook access on failure
    request.node.driver = driver_instance
    yield driver_instance
    driver_instance.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver_instance = getattr(item, "driver", None)
        if driver_instance:
            screenshot_dir = Path("reports/screenshots")
            screenshot_dir.mkdir(parents=True, exist_ok=True)
            screenshot_path = screenshot_dir / f"{item.name}.png"
            driver_instance.save_screenshot(str(screenshot_path))
            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html:
                extra = getattr(report, "extra", [])
                extra.append(pytest_html.extras.image(str(screenshot_path)))
                report.extra = extra
