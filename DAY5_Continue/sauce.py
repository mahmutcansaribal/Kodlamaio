from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#Bekleme işlemlerini ele alacak kütüphanedir.
from selenium.webdriver.support.wait import WebDriverWait
#İlgili bekleme işlemlerini yaparken hangi şarta olarak bekleneceğini söyler.
from selenium.webdriver.support import expected_conditions as ec

class Test_Sauce:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")

    #Eski yapımız
    def test_invalid_login(self):
        
        #Maksimum 5 saniye.
                #Until; ne zamana kadar ...  şuna kadar bekle.
                #Visibility: görünür olma durumu.
        # En fazla 5 saniye olacak şekilde user-name id'li elementin görünmesini bekle.
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))

        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
    

        usernameInput = self.driver.find_element(By.ID,"user-name")
        passwordInput = self.driver.find_element(By.ID,"password")

        usernameInput.send_keys("1")
        passwordInput.send_keys("1")

        loginBtn = self.driver.find_element(By.ID,"login-button")

        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"Test Sonucu : {testResult}")

    #Yeni yapımız.
    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,"password")
        
        
        # Action Chains ; Aksiyonlarımızı zincir misali arka arkaya bağlamamızı sağlayan bir yapıdır.

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        #Zincir olarak birbiri ardına çalışacaklardır.
        actions.perform()
        # usernameInput.send_keys("standard_user")
        # passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(10)
testClass = Test_Sauce()
testClass.test_invalid_login()
testClass.test_valid_login()