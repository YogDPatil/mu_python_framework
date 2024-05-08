import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ConfirmPage:

    locationField = (By.ID, "country")
    selLocation = (By.LINK_TEXT, "India")
    purchaseBtn = (By.XPATH, "//input[@type='submit']")
    successMsg = (By.XPATH, "//div[contains(@class,'dismissible')]")

    def __init__(self, driver):
        self.driver = driver


    def locationFieldEle(self):
        return self.driver.find_element(*ConfirmPage.locationField)

    def selectLocation(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.presence_of_element_located(ConfirmPage.selLocation))
        #time.sleep(5)
        return self.driver.find_element(*ConfirmPage.selLocation)

    def purchaseButtonEle(self):
        return self.driver.find_element(*ConfirmPage.purchaseBtn)

    def orderSuccessfulMsg(self):
        return self.driver.find_element(*ConfirmPage.successMsg)