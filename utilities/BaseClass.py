import inspect
import logging

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

    def getLogger(self):
        # set name as method name
        loggerName = inspect.stack()[1][3]
        # getLogger used to get log file and __name__ is for name of test file
        logger = logging.getLogger(loggerName)

        # FileHandler is for locating log file
        fileHandler = logging.FileHandler('/Users/codeclouds-yogesh/Documents/MythonDemoVENV/PythonFamework/logFile.log')
        # format log file name
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        # ste level so from which level logging is required : level hierarchy-> debug>info>warning>error>critical
        logger.setLevel(logging.DEBUG)
        return logger