from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
#Selenium nedir? : Herhangi bir tarayıcıyı açtığımızda geziniriz. Butonlara tıklarız inputlara tıklarız url değiştiririz vs bu yaptığımız manuel işlemlerin otomatize yapılmasını sağlayan bir yapıdır. Selenium her dilde kullanılabilen bir yapıdır.

# Eğer driver hata verirse : https://chromedriver.chromium.org/downloads
# pip install webdriver-manager
#DAY 4 devam
driver = webdriver.Chrome(ChromeDriverManager().install())
# Ekranı tam erkan yapar.
driver.maximize_window()
# İstediğimiz Url' e yönlendirir.
driver.get("https://www.google.com/")
sleep(1)
input = driver.find_element(By.NAME , "q")
print(f"INPUT : {input} ")
input.send_keys("kodlamaio")
sleep(1)


searchButton = driver.find_element(By.NAME , "btnK")
sleep(1)
searchButton.click()


sleep(1)
# Aramadan sonra çıkan ilk sonucu bulur.
firstResult = driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a")
sleep(1)
firstResult.click()


listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlamaio sitesinde şu anda : {len(listOfCourses)} adet kurs vardır.")

#sleep(10)

while True:
    continue
# HTML LOCATORS : Konum öğrenme.

# XPATH 
# //*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a

# FULL -XPATH
# /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a

