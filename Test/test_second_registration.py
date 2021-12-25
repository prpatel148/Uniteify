import time

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.RegistrationPage import RegistrationPage
from TestData.RegistrationData import RegistrationData
from Utility.Baseclass import BaseClass


class TestRegistration(BaseClass):

    def test_Registration(self, getData):
        log = self.getLogger()
        registrationPage = RegistrationPage(self.driver)

        registrationPage.clickRegister().click()

        if getData["gender"] == "Female":
            registrationPage.getGenderF().click()

        registrationPage.getUsername().click()
        if getData["username"] == None:
            registrationPage.getKnownas().click()
        else:
            registrationPage.getUsername().send_keys(getData["username"])

        registrationPage.getKnownas().click()
        if getData["knownas"] == None:
            registrationPage.getCity().click()
        else:
            registrationPage.getKnownas().send_keys(getData["knownas"])

        if getData["birthdate"] == None:
            registrationPage.getCity().click()
        else:
            registrationPage.getBirthdate().send_keys(getData["birthdate"])

        registrationPage.getCity().click()
        if getData["city"] == None:
            registrationPage.getCountry().click()
        else:
            registrationPage.getCity().send_keys(getData["city"])

        registrationPage.getCountry().click()
        if getData["country"] == None:
            registrationPage.getPassword().click()
        else:
            registrationPage.getCountry().send_keys(getData["country"])

        registrationPage.getPassword().click()
        if getData["password"] == None:
            registrationPage.confrimPassword().click()
        else:
            registrationPage.getPassword().send_keys(getData["password"])

        registrationPage.confrimPassword().click()
        if getData["confirmPass"] == None:
            self.driver.refresh()
        else:
            registrationPage.confrimPassword().send_keys(getData["confirmPass"])







        # registrationPage.getCity().click()
        # registrationPage.getCity().send_keys(getData["city"])
        # registrationPage.getCountry().click()
        # registrationPage.getCountry().send_keys(getData["country"])
        # registrationPage.getPassword().click()
        # registrationPage.getPassword().send_keys(getData["password"])
        # registrationPage.confrimPassword().click()
        # registrationPage.confrimPassword().send_keys(getData["confirmPass"])
        # registrationPage.clickSubmit().click()
        # registrationPage.clickCancel().click()



    @pytest.fixture(params=RegistrationData.getTestdata("test3"))
    def getData(self, request):
        return request.param








