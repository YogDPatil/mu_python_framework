import time

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_verifyFormFillSuccessfully(self):
        homepage = HomePage(self.driver)
        homepage.enterName('Yogesh')
        homepage.enterEmail('ydp')
        homepage.enterPassword('pass')
        self.selectValueFromDropByText(homepage.genderDropdown(), 'Female')
        homepage.clickOnSubmitButton()
        time.sleep(5)

