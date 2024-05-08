from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class ShopPage:

    productsList = (By.XPATH, "//div[@class='card h-100']")
    #productNames = (By.XPATH, "div/h4/a")
    checkoutBtn = (By.XPATH, "//a[contains(@class, 'btn-primary')]")

    def __init__(self, driver):
        self.driver = driver


    def getProductsList(self):
        return self.driver.find_elements(*ShopPage.productsList)

    #def getProductNames(self):
    #    return self.driver.find_element(*ShopPage.productNames)
    #    #return self.driver.find_element(*ShopPage.productNames)

    def chekoutButtonLink(self):
        self.driver.find_element(*ShopPage.checkoutBtn).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage