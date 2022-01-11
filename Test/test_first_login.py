import time

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

        # Test Case 1 - Case Scenario - invalid username and valid password
        loginPage.enterUsername().send_keys("jana123")
        loginPage.enterPassword().send_keys("Hcl@1234")
        loginPage.clickLogin().click()
        error = WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[id = 'toast-container']"))).text
        assert "Invalid" in error
        self.driver.refresh()

        # Test Case 2 - Case Scenario - valid username and invalid password
        loginPage.enterUsername().send_keys("jana")
        loginPage.enterPassword().send_keys("Hcl@1234567")
        loginPage.clickLogin().click()
        error = WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[id = 'toast-container']"))).text
        assert "Invalid" in error
        self.driver.refresh()

        # Test Case 3 - Case Scenario - invalid username(case sensitive) and valid password
        loginPage.enterUsername().send_keys("JANA")
        loginPage.enterPassword().send_keys("Hcl@1234")
        loginPage.clickLogin().click()
        error = WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[id = 'toast-container']"))).text
        assert "Invalid" in error
        self.driver.refresh()

        # Test Case 4 - Case Scenario - valid username and invalid password(case sensitive)
        loginPage.enterUsername().send_keys("jana")
        loginPage.enterPassword().send_keys("HCL@1234")
        loginPage.clickLogin().click()
        error = WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[id = 'toast-container']"))).text
        assert "Invalid" in error
        self.driver.refresh()

        # Test Case 5 - Case Scenario - EMPTY username and valid password
        loginPage.enterUsername().send_keys("")
        loginPage.enterPassword().send_keys("Hcl@1234")
        loginPage.clickLogin().click()
        error = WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[id = 'toast-container']"))).text
        assert "Invalid" in error
        self.driver.refresh()

        # Test Case 6 - Case Scenario - valid username and EMPTY password
        loginPage.enterUsername().send_keys("jana")
        loginPage.enterPassword().send_keys("")
        loginPage.clickLogin().click()
        error = WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[class='container'] h5"))).text
        assert "Internal Server Error" in error
        self.driver.refresh()

        #Test Case 7 - Case Scenario - valid username and valid password
        loginPage.enterUsername().send_keys("jana")
        loginPage.enterPassword().send_keys("Hcl@1234")
        loginPage.clickLogin().click()
        time.sleep(1)
        self.driver.refresh()


        # error = WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[id = 'toast-container']"))).text
        #
        # assert "Invalid" in error
        # self.driver.refresh()
