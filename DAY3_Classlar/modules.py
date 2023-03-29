import matematik as math
#built-in modules
import random 

from Classes import Human
# sadece istediğimiz kısmı import etmek istiyorsak onu import ediyoruz yani mesela burada toplayı değil sadece bolme fonksiyonunu kullanmak istiyoruz.
from matematik import bol

from selenium import webdriver

print(math.topla(10,20))

print(random.randint(0,100))

human1 = Human("Hira")
human1.talk("Merhaba")



#packages.

chromeDrive = webdriver.Chrome()

