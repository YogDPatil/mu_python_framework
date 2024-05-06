import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


# here no need to use @pytest.mark.usefixtures("setup") because we use inheritace of base class
# in which we use @pytest.mark.usefixtures("setup")
#@pytest.mark.usefixtures("setup")
class TestFirst(BaseClass):

    def test_e2e(self):
        self.driver.implicitly_wait(4)

        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text

            if productName == "Nokia Edge":
                product.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.XPATH, "//a[contains(@class, 'btn-primary')]").click()
        selectedProduct = self.driver.find_element(By.XPATH, "//h4[@class='media-heading']/a").text

        assert selectedProduct == "Nokia Edge"
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys('ind')

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        print(self.driver.find_element(By.XPATH, "//div[contains(@class,'dismissible')]").text)
        message = self.driver.find_element(By.XPATH, "//div[contains(@class,'dismissible')]").text

        assert "Success! Thank you!" in message

        #self.driver.close()

