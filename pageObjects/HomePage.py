from selenium.webdriver.common.by import By

from pageObjects.ShopPage import ShopPage


class HomePage:
    shop = (By.LINK_TEXT, "Shop")

    def __init__(self, driver):
        self.driver = driver

    def clickOnShopPageLink(self):
        self.driver.find_element(*HomePage.shop).click()
        shopPage = ShopPage(self.driver)
        return shopPage