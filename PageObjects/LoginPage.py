from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.CSS_SELECTOR, "input[name='username']")
    password = (By.CSS_SELECTOR, "input[name='password']")
    button = (By.CSS_SELECTOR, "button[type='submit']")

    def enterUsername(self):
        return self.driver.find_element(*LoginPage.username)

    def enterPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def clickLogin(self):
        return self.driver.find_element(*LoginPage.button)





# toast messsage html :::: 401 unauthorized

# <div id="toast-container" class="toast-bottom-right toast-container" xpath="1">
# <div class="ng-tns-c35-12 ng-star-inserted ng-trigger ng-trigger-flyInOut ngx-toastr toast-error"
#     toast-component="" style="opacity: 1;"><!----><div class="ng-tns-c35-12 toast-title ng-star-inserted"
#     aria-label="401" style=""> 401 <!----></div><!----><!----><div role="alertdialog" aria-live="polite"
#     class="ng-tns-c35-12 toast-message ng-star-inserted" aria-label="Unauthorized" style=""> Unauthorized
#     </div><!----><!----></div></div>


