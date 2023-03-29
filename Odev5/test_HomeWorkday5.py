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

#Odev 5 ekle.

class Test_HomeWorkDay5:
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
    
    def ClickButton(self):
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()


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

    @pytest.mark.parametrize("username,password",[("locked_out_user","secret_sauce")])
    def test_TryNameAndPassowrd(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"user-name"))
        passwordInput = self.driver.find_element(By.ID,"password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        self.ClickButton()
        
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/TryNameAndPassword-Blank-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
    
    @pytest.mark.parametrize("username,password",[("","")])
    def test_XImage(self,username,password):
        
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        self.ClickButton()

        self.waitForElementVisible((By.CLASS_NAME,"error-button"))
        errorBtn = self.driver.find_element(By.CLASS_NAME,"error-button")
        self.driver.save_screenshot(f"{self.folderPath}/XImage-Blank-{username}-{password}.png")
        errorBtn.click()
        
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_UrlGetAndProductList(self,username,password):
         
         self.waitForElementVisible((By.ID,"user-name"))
         usernameInput = self.driver.find_element(By.ID,"user-name")
         self.waitForElementVisible((By.ID,"user-name"))
         passwordInput = self.driver.find_element(By.ID,"password")

         usernameInput.send_keys(username)
         passwordInput.send_keys(password)

         self.ClickButton()

         self.driver.get("https://www.saucedemo.com/inventory.html")
         
         listOfProducts = self.driver.find_elements(By.CLASS_NAME,"inventory_item")

         print(f"Sauce sitesinde şu anda : {len(listOfProducts)} adet ürün vardır.")
         self.driver.save_screenshot(f"{self.folderPath}/ProductList-Blank-{username}-{password}.png")

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_AddToChart(self,username,password):

        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"user-name"))
        passwordInput = self.driver.find_element(By.ID,"password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        self.ClickButton()

        self.waitForElementVisible((By.ID,"add-to-cart-sauce-labs-backpack"))
        addBtn = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        addBtn.click()

        self.driver.save_screenshot(f"{self.folderPath}/AddToChart-Blank-{username}-{password}.png")

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_AddShop(self,username,password):

        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"user-name"))
        passwordInput = self.driver.find_element(By.ID,"password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        self.ClickButton()

        self.waitForElementVisible((By.ID,"add-to-cart-sauce-labs-backpack"))
        addBtn = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        addBtn.click()

        self.waitForElementVisible((By.CLASS_NAME,"shopping_cart_link"))
        shopButton =self.driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        shopButton.click()
        self.driver.save_screenshot(f"{self.folderPath}/AddShop-{username}-{password}.png")
    
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_CompleteShopping(self,username,password):
        

        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"user-name"))
        passwordInput = self.driver.find_element(By.ID,"password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        self.ClickButton()

        self.waitForElementVisible((By.ID,"add-to-cart-sauce-labs-backpack"))
        addBtn = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        addBtn.click()

        self.waitForElementVisible((By.CLASS_NAME,"shopping_cart_link"))
        shopButton =self.driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        shopButton.click()

        self.waitForElementVisible((By.ID,"checkout"))
        checkButton = self.driver.find_element(By.ID,"checkout")
        checkButton.click()

        self.waitForElementVisible((By.ID,"first-name"))
        firstName = self.driver.find_element(By.ID,"first-name")
        self.waitForElementVisible((By.ID,"last-name"))
        lastName = self.driver.find_element(By.ID,"last-name")
        self.waitForElementVisible((By.ID,"last-name"))
        zipCode = self.driver.find_element(By.ID,"postal-code")

        firstName.send_keys("Mahmut Can")
        lastName.send_keys("Saribal")
        zipCode.send_keys("34000")

        self.waitForElementVisible((By.ID,"continue"))
        continueBtn = self.driver.find_element(By.ID,"continue")
        continueBtn.click()

        self.waitForElementVisible((By.ID,"finish"))
        finistBtn = self.driver.find_element(By.ID,"finish")
        finistBtn.click()

        self.driver.save_screenshot(f"{self.folderPath}/CompleteShop-{username}-{password}.png")

    @pytest.mark.parametrize("username,password",[("1","1"),("standard_user",""),("standard_user","secret_sauce")])
    def test_TreeTryUser(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"user-name"))
        passwordInput = self.driver.find_element(By.ID,"password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        self.ClickButton()
        self.driver.save_screenshot(f"{self.folderPath}/TreeTryUser-{username}-{password}.png")
        
    

    