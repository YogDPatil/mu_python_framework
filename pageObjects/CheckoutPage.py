from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    selectedProduct = (By.XPATH, "//h4[@class='media-heading']/a")
    checkoutBuyBtn = (By.XPATH, "//button[@class='btn btn-success']")
    def __init__(self, driver):
        self.driver = driver

    def getSelectedProject(self):
        return self.driver.find_element(*CheckoutPage.selectedProduct)

    def checkoutBuyBttton(self):
        self.driver.find_element(*CheckoutPage.checkoutBuyBtn).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage