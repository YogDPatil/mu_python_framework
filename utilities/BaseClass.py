import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def waitTillPresenceOfElementLocated(self, locator):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.presence_of_element_located(locator))

    def selectValueFromDropByText(self, element, text):
        sel = Select(element)
        sel.select_by_visible_text(text)