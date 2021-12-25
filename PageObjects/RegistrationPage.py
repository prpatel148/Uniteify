from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    register = (By.CSS_SELECTOR, "button[class='btn btn-primary btn-lg mr-2']")
    # 1
    gender = (By.CSS_SELECTOR, "input[value='female']") # for female
    username = (By.CSS_SELECTOR, "div[class='form-group'] input[placeholder='Username']")
    knownAs = (By.CSS_SELECTOR, "input[placeholder='Known As']")
    dOb = (By.CSS_SELECTOR, "input[placeholder='Date Of Birth']")
    city = (By.CSS_SELECTOR, "input[placeholder='City']")
    country = (By.CSS_SELECTOR, "input[placeholder='Country']")
    password = (By.CSS_SELECTOR, "div[class='form-group'] input[placeholder='Password']")
    confirmP = (By.CSS_SELECTOR, "div[class='form-group'] input[placeholder='Confirm Password']")
    submit = (By.CSS_SELECTOR, "button[class='btn btn-success mr-2']")
    cancel = (By.CSS_SELECTOR, "button[class='btn btn-primary mr-2']")
    #10

    def clickRegister(self):
        return self.driver.find_element(*RegistrationPage.register)

    def getGenderF(self):
        return self.driver.find_element(*RegistrationPage.gender)

    def getUsername(self):
        return self.driver.find_element(*RegistrationPage.username)

    def getKnownas(self):
        return self.driver.find_element(*RegistrationPage.knownAs)

    def getBirthdate(self):
        return self.driver.find_element(*RegistrationPage.dOb)

    def getCity(self):
        return self.driver.find_element(*RegistrationPage.city)

    def getCountry(self):
        return self.driver.find_element(*RegistrationPage.country)

    def getPassword(self):
        return self.driver.find_element(*RegistrationPage.password)

    def confrimPassword(self):
        return self.driver.find_element(*RegistrationPage.confirmP)

    def clickSubmit(self):
        return self.driver.find_element(*RegistrationPage.submit)

    def clickCancel(self):
        return self.driver.find_element(*RegistrationPage.cancel)


# toast messsage html :::: 401 unauthorized

# <div id="toast-container" class="toast-bottom-right toast-container" xpath="1">
# <div class="ng-tns-c35-12 ng-star-inserted ng-trigger ng-trigger-flyInOut ngx-toastr toast-error"
#     toast-component="" style="opacity: 1;"><!----><div class="ng-tns-c35-12 toast-title ng-star-inserted"
#     aria-label="401" style=""> 401 <!----></div><!----><!----><div role="alertdialog" aria-live="polite"
#     class="ng-tns-c35-12 toast-message ng-star-inserted" aria-label="Unauthorized" style=""> Unauthorized
#     </div><!----><!----></div></div>


