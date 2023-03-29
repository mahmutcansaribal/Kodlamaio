faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

# Tip Dönüşümü.
print(int(vade)+12)
#print(int(krediadi))
faiz = str(faiz)
print(type(faiz))

# Kullanicidan girdisi alma.

vade = 30 #int(input("Lütfen istediğiniz vade sayisini giriniz : "))
vade = vade + 12

# String interpolation
# Seçtiğiniz vade sonucu ortaya cikan vade : {}

print("Seçtiğiniz vade sonucu ortaya cikan vade : "+str(vade))

print("Seçtiğniz vade sonucu : {vadeSayisi}".format(vadeSayisi=vade))



isim = "Halit"
metin = "Merhaba {name}".format(name = isim)
print(metin)

# f-string

metin = f"Hoşgeldiniz {isim}"
print(metin)

# Listeler
# Döngüler
# Fonksiyonlar

dizi = ["İhtiyaç kredisi",10,5.2,True]
print(dizi)

krediler = ["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
print(type(krediler))
print(krediler[0])
print(len(krediler))
krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("Taşı Kredisi")
print(krediler)

#Gördüğü ilk değeri siler.
krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["Y kredisi","Z kredisi"])
print(krediler)

# For döngüsü
for i in range(10):
    print(i)
print("---------------")
# 5 sayısından başlar 10'a kadar gider 10 dahil edilmez.
for i in range(5,10):
    print(i)
print("---------------")
# 0 = baslangic 51 e kadar gider 10'ar 10'ar artarak.
for i in range(0,51,10):
    print(i)
print("---------------")

# for i in range(0.1,0.5):
#     print(i)

krediler = ["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]

for kredi in krediler:
    print(kredi)

print("---------------")

for i in range(len(krediler)):
    print(krediler[i])

print("---------------")

while i<10:
    print("x")
    i = i + 1
print(i)
print("--------SON DÖNGÜ--------")
i=0
while i < len(krediler):
    i+=1
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break
    
# Fonksiyonlar.

fiyat = 100
indirim = 20

#değer döndürmeyen

def calculate(a,b):
    print(a-b)


def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)
calculateWithParams(50,20)

def sayHello(name):
    print(f"Merhaba {name}")
sayHello("mahmut can")

def calculateAndReturn(price,discount):
    return price-discount


yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)

print("merhaba")

