# Öğrenci Kayıt Sistemi MAHMUT CAN SARIBAL


ogrenciListesi = list()
def tekbirOgrenciEkle():
    ogrenciAdSoyad = input("Ogrencinin Adi SoyAdi Giriniz : ")
    ogrenciListesi.append(ogrenciAdSoyad)

def tekbirOgrenciSil():
    OgrenciSil = input("Silinecek Ogrencinin Adini SoyAdini giriniz : ")
    ogrenciListesi.remove(OgrenciSil)

def ogrencileriListele():
    for i in range (len(ogrenciListesi)):
        print(ogrenciListesi[i])

def TopluEkle():
    while True:
        isimEkle = input("'Dur' yazana kadar girilen ogrenci isimleri listeye eklenecektir.\n")
        if isimEkle == "Dur":
             break
        ogrenciListesi.append(isimEkle)

def TopluSil():
    while True:
        isimSil = input("'Dur' yazana kadar girilen ogrenci isimler listeden silinecektir.\n")
        if isimSil == "Dur":
            break
        elif isimSil in ogrenciListesi:
            print("Yanlis Ogrenci ismi girdiniz!")
        ogrenciListesi.remove(isimSil)

def OgrenciNumarasiGetir():
    arama = input("Öğrenci Numarasını Öğrenmek istediğiniz Öğrencinin Adını SoyAdını giriniz : ")
    i = 0
    while i<= len(ogrenciListesi):
        try:
            if ogrenciListesi[i] == arama:
                print(i)
                break
            i+=1
        except:
            print("Böyle bir öğrenci yok")

while True:
    print("1- Tek bir Ogrenci Ekleme\n2- Tek bir Ogrenci Silme\n3- Ogrencileri Listele\n4- Toplu Ogrenci Ekleme\n5- Toplu Ogrenci Silme\n6- Ogrenci Numarasına göre öğrenci arama\n7- Cikis")
    secim = input("Secim : ")
    if secim == "1":
        tekbirOgrenciEkle()

    elif secim == "2":
        tekbirOgrenciSil()

    elif secim == "3":
        ogrencileriListele()

    elif secim == '4':
        TopluEkle()
        
    elif secim == '5':
        TopluSil()

    elif secim == '6':
        OgrenciNumarasiGetir()

    elif secim == '7':
        print("Cikis yapiliyor...")
        break

