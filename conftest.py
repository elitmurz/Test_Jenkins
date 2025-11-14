import driver
import pytest
from selene.core._browser import Browser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser, Config, Browser


@pytest.fixture(scope="function")
def setup_browser(request):
    from selenium import webdriver

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    driver = webdriver.Remote(
        command_executor="https://selenoid.autotests.cloud/wd/hub",
        desired_capabilities=capabilities)

    browser: Browser= Browser(Config(driver))
    yield browser