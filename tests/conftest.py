import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope = "class")
def setup(request):
    chromdriverPath = Service("/Users/codeclouds-yogesh/Downloads/chromedriver-mac-arm64/chromedriver")
    driver = webdriver.Chrome(service=chromdriverPath)
    driver.get("https://rahulshettyacademy.com/angularpractice/shop")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

