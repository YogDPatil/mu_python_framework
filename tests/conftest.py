import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# this code is for to select browser from terminal
# and make chrome default if not selected
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action = "store", default = "chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    # below line code is connect browser_name from terinal to this code
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        chromdriverPath = Service("/Users/codeclouds-yogesh/Downloads/chromedriver-mac-arm64/chromedriver")
        driver = webdriver.Chrome(service=chromdriverPath)
    elif browser_name == "firefox":
        geckodriverPath = Service("/Users/codeclouds-yogesh/Downloads/geckodriver")
        driver = webdriver.Firefox(service=geckodriverPath)
    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

