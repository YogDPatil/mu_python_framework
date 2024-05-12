import time

import pytest

from pageObjects.HomePage import HomePage
from testData.homePageData import homePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_verifyFormFillSuccessfully(self, getHomePageData):
        homepage = HomePage(self.driver)
        homepage.enterName(getHomePageData['fName'])
        homepage.enterEmail(getHomePageData['email'])
        homepage.enterPassword(getHomePageData['pass'])
        self.selectValueFromDropByText(homepage.genderDropdown(), getHomePageData['gender'])
        homepage.clickOnSubmitButton()
        time.sleep(3)


    #@pytest.fixture(params = [("Yogesh", 'ydp' , 'pass', 'Male'), ('Tejal', 'teju', 'pass', 'Female')])
    #def getHomePageData(self, request):
    #    return request.param


    # here use parameter of fixture as dictionary for more readble formate
    @pytest.fixture(params=homePageData.testHomePageData)
    def getHomePageData(self, request):
        return request.param
