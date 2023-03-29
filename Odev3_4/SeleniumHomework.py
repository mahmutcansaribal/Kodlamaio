from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
             
class TestSauceSite:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        sleep(2)
    
    def UsernameAndPasswordBlanKTest(self):
        usernameInput = self.driver.find_element(By.ID,"user-name")
        passwordInput = self.driver.find_element(By.ID,"password")
        sleep(2)

        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)

        loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)

        loginBtn.click()
        sleep(2)

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"

        if testResult == True:
            print(f"Error Message : {testResult} - Epic sadface: Username is required")
            
    def OnlyPasswordBlankTest(self):
        usernameInput = self.driver.find_element(By.ID,"user-name")
        passwordInput = self.driver.find_element(By.ID,"password")
        sleep(2)

        usernameInput.send_keys("Mahmut Can")
        passwordInput.send_keys("")
        sleep(2)

        loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)

        loginBtn.click()
        sleep(2)

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"

        if testResult == True:
            print(f"Error Message : {testResult} - Epic sadface: Password is required")

    def TryNameAndPassword(self):
        usernameInput = self.driver.find_element(By.ID,"user-name")
        passwordInput = self.driver.find_element(By.ID,"password")
        sleep(2)

        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)

        loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)

        loginBtn.click()
        sleep(2)

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

        if testResult == True:
            print(f"Error Message : {testResult} - Epic sadface: Sorry, this user has been locked out.")

    def xImage(self):

        try:
            usernameInput = self.driver.find_element(By.ID,"user-name")
            passwordInput = self.driver.find_element(By.ID,"password")
            sleep(2)

            usernameInput.send_keys("")
            passwordInput.send_keys("")
            sleep(2)

            loginBtn = self.driver.find_element(By.ID,"login-button")
            sleep(2)
            loginBtn.click()
            sleep(2)

            errorBtn = self.driver.find_element(By.CLASS_NAME,"error-button")
            sleep(2)
            errorBtn.click()
            sleep(2)
        except:
            print("Hata var!")
        
    def UrlGetAndProductList(self):

        usernameInput = self.driver.find_element(By.ID,"user-name")
        passwordInput = self.driver.find_element(By.ID,"password")
        sleep(2)

        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)

        loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)

        loginBtn.click()
        sleep(2)

        self.driver.get("https://www.saucedemo.com/inventory.html")
        sleep(2)

        listOfProducts = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        sleep(1)

        print(f"Sauce sitesinde şu anda : {len(listOfProducts)} adet ürün vardır.")


testClass = TestSauceSite()
testClass.xImage()
