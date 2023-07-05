
# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
print("Soru 1")
def yazdir(kelime,adet):
    print(kelime * adet)

yazdir("Merhaba\n",10)   # \n bir alt satıra geçmek için kullanılır.
print()


# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.
print("Soru 2")
def listeyeCevir(*params):   #Sınırsız sayıda paremetre olduğunu belirtmek için * kullanılır
    liste = []

    for param in params:
        liste.append(param)

    return liste

cikti = listeyeCevir(10,20,30,"Merhaba","Hakan Akıncı","Bozdoğan Roket")
print(cikti)
print()


# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
print("Soru 3")
def asalSayilariBulma(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi > 1:
            for i in  range(2,sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

sayi1 = int(input("Sayı1: "))
sayi2 = int(input("Sayı2: "))

asalSayilariBulma(sayi1,sayi2)
print()


# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.
print("Soru 4")
def tamBolunenleriBul(sayi):
    tamBolenler = []

    for i in range(2,sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)

    return tamBolenler

print(tamBolunenleriBul(50))
print()

