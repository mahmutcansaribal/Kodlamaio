'''PYTHON VERİ TÜRLERİ'''

#String
'''Boolean veri tipi
 Mantiksal bir veri tipidir. False ya da True degerleri karsilik gelir
'''
dogru = True
print(type(dogru))
'''String veri tipi metinsel ifadeler içi n kullanılır.'''

isim = "Mahmut Can Sarıbal" #String 

''' Numerik sayı tipleri (int,float,complex,Long) sayıları ifade etmek için kullanılır

1- Int => Tam sayılar için kullanılır.
2- Float/Double => Ondalıklı sayılar için kullanilir.
3- Complex => Karmaşık sayılar için
3- Long => Çok daha uzun tam sayılar için
'''
tamSayi = 1
print(type(tamSayi))
ondalikSayi = 3.4
print(type(ondalikSayi))
complexSayi = complex(1,3)
print(type(complexSayi))

''' Siralama Veri Tipleri 

1- List => List birbirinden farkli veri tipine sahip ögeleri barindirabilen sirali ve degistirilebilir veri tipidir. [] ile kullanilir.

2- Tuple => list veri tipi gibi sıralı ögelerden oluşan veri tipidir. Tuple ile list arasındaki fark ise tuple’ın değiştirilemez olmasıdır. Tuple ( ) içerisine yazılan değerler ile tanımlanır.

3- Dictionary => Anahtar ve key ilişkisi vardır {} ile gösterilir.

'''

listVeriTipi = [1,2,"Merhaba",3.4]
print(type(listVeriTipi))

tupleVeriTipi = (5,4,3,"Merhaba",4.3)
print(type(tupleVeriTipi))

DictionaryVeriTipi = {
    "Adi" : "Mahmut Can",
    "SoyAdi" : "Saribal"
}

print(type(DictionaryVeriTipi))


'''ŞART BLOKLARI KISMI'''

#Kodlamaio örnegin yoklama kısmını tamamlamadan ödev1'e geçme kısmı bir şarttır yoklama tamamlandıysa ödev1'e geçilir.
#Aynı şekilde ödev1 tamamlandiysa ödev2'ye geçilir

ogrenciAdi = "Mahmut Can"
yoklama = True
odev1 = True
odev2 = False

if ogrenciAdi == "Mahmut Can" and yoklama == True:
    print("Ogrenci adi ve yoklama tamamlanmistir")
    if odev1 == True:
        print("Odev 1 tamamlandi Tebrikler. Şimdi devam edebilirisiniz!")
        
        if odev2 == True:
             print("Odev 2 tamamlandi Tebrikler. Şimdi devam edebilirisiniz!")
        else:
            print("Önce Odev 2'i tamamlamalısınız.")
    else:
        print("Önce Odev 1'i tamamlamalısınız.")
else:
    print("Odev 1 e geçmek için yoklamanızı tamamlayiniz.")
