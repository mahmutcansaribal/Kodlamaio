from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date

#Bekleme işlemlerini ele alacak kütüphanedir.
from selenium.webdriver.support.wait import WebDriverWait
#İlgili bekleme işlemlerini yaparken hangi şarta olarak bekleneceğini söyler.
from selenium.webdriver.support import expected_conditions as ec



class Test_HomeWorDay5:
    #Her Testten önce çagrilir.
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

        # günün tarihi al bu tarih ile bir klasör var mı kontrol et yoksa oluştur.
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True,)

    #her testten sonra çağrılır.
    def teardown_method(self):
        self.driver.quit()
        
    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(locator))

    @pytest.mark.parametrize("username,password",[("","")])
    def test_UsernameAndPasswordBlanKTest(self,username,password):
        
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/UsernameAndPassword-Blank-{username}-{password}.png")
        
        assert errorMessage.text == "Epic sadface: Username is required"
    
    @pytest.mark.parametrize("username,password",[("MahmutCan","")])
    def test_OnlyPasswordBlankTest(self,username,password):

        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"user-name"))
        passwordInput = self.driver.find_element(By.ID,"password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/OnlyPasswordBlank-{username}-{password}.png")

        assert errorMessage.text == "Epic sadface: Password is required"