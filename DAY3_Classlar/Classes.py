
class Human:
    #Built-in (Ctor) #constructor #initialize
    def __init__(self,name) -> None:
        self.name = name;
        print("Bir human instance'i üretildi.")
    
    def __str__(self):
        return f"STR fonksiyonundan dönen değer : {self.name}"

    def talk(self,sentence):
        #self keyword kullanarak diğer alanlara erişiyoruz.
        print(f"{self.name} : {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")

# instance => örnek 
# self =>  this keyword olarak düşünmeliyiz. Bu ilgili fonksiyonun kendisini ifade eder. İlk Parametre self parametresi ile rezerve edilir. Class içersinde fonksiyon kullanıyorsak self parametresi kullanmak zorundayız self vermek zorunda değiliz.
human1 = Human("Enes")
human1.talk("Merhaba")
human1.walk()
print(human1)
print("---------------")
human2 = Human("Mehmet")
human2.talk("Selam")
human2.walk()
print(human2)
