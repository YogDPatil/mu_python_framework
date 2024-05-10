from selenium.webdriver.common.by import By

from pageObjects.ShopPage import ShopPage


class HomePage:
    shop = (By.LINK_TEXT, "Shop")
    nameField = (By.XPATH, "//div[@class='form-group']//input[@name='name']")
    emailField = (By.NAME, "email")
    passwordField = (By.XPATH, "//input[@id='exampleInputPassword1']")
    submitBtn = (By.XPATH, "//input[@type='submit']")
    genderDrop = (By.ID, "exampleFormControlSelect1")


    def __init__(self, driver):
        self.driver = driver

    def clickOnShopPageLink(self):
        self.driver.find_element(*HomePage.shop).click()
        shopPage = ShopPage(self.driver)
        return shopPage

    def enterName(self, name):
        self.driver.find_element(*HomePage.nameField).send_keys(name)

    def enterEmail(self, email):
        self.driver.find_element(*HomePage.emailField).send_keys(email)

    def enterPassword(self, password):
        self.driver.find_element(*HomePage.passwordField).send_keys(password)

    def genderDropdown(self):
        return self.driver.find_element(*HomePage.genderDrop)

    def clickOnSubmitButton(self):
        return self.driver.find_element(*HomePage.submitBtn).click()