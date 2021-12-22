import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage import LoginPage
from Utility.Baseclass import BaseClass


class TestLogin(BaseClass):

    def test_formSubmission(self):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        # log.info("Name is "+getData["name"])
        loginPage.enterUsername().send_keys("jana")
        loginPage.enterPassword().send_keys("Hcl@1234")
        loginPage.clickLogin().click()
        # print(loginPage.errorMsg().text)
        # message = self.driver.find_elements_by_css_selector("div[id = 'toast-container']").text
        # print(message)

        error = WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[id = 'toast-container']"))).text

        assert "Invalid" in error
        # self.driver.refresh()

    # @pytest.fixture(params=HomePageData.getTestdata("test2"))
    # def getData(self, request):
    #     return request.param


