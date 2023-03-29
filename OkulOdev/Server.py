import socket


host = "localhost"
port = 8010
#AF_INET : TCP VE UDP ICIN PIV4 PROTOKOL.

try:
    firstSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket yaratıldı.")
    firstSocket.bind((host,port))

    print(f"socket {port} nolu porta baglandi")
    #En fazla 3 baglantiya izin verir.
    firstSocket.listen(3)
    print("socket dinleniyor.")
except socket.error as msg:
    print("Hata :",msg)

while True:

    #Client ile baglanti konfigürasyon.
    c, addr = firstSocket.accept()
    print("Gelen baglanti : ",addr)

    #Baglanan client tarafına mesaj.
    mesaj = "Baglanti sağlandi.."
    c.send(mesaj.encode('utf-8'))
    c.close()