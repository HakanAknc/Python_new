sayilar = [1,3,5,7,9,12,19,21]

# 1) sayilar listesini while ile ekrana yazdırın.
print("Soru 1")
"""
while sayilar:
    print(sayilar)
    break
"""
i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1
print()


# 2) Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#    tek sayıları ekrana yazdırın.
print("Soru 2")
baslangic = int(input("Başlangıçı girin: "))
bitis = int(input("Bitişi girin: "))

i = baslangic
while i < bitis:
    i += 1
    if (i % 2 == 1):
        print(i)
print()


# 3) 1-100 arasındaki sayıları azalan şekilde yazdırın.
print("Soru 3")
i = 100
while i > 0:
    print(i)
    i -= 1
print()


# 4) Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın
print("Soru 4")
numbers = []
i = 0
while i < 5:
    sayi = int(input("Sayı giriniz: "))
    numbers.append(sayi)   #diziye ekler
    i += 1
numbers.sort()
print(numbers)
print()


# 5) Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.
print("Soru 5")
urunler = []

adet = int(input("Kaç ürün eklemek istiyorsunuz: "))
i = 0

while (i<adet):
    name = input("Ürün ismi: ")
    fiyat = input("Ürün fiyatı: ")
    urunler.append({
        "name": name,
        "fiyat": fiyat
    })
    i += 1

for urun in urunler:
    print(f"Ürün adı: {urun['name']} Ürün fiyatı: {urun['fiyat']}")
