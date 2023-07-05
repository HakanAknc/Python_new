sayilar = [1,3,2,7,4,12,19,21]

# 1) Sayilar listesindeki hangi sayılar 3'ün katıdır ?
print("Soru 1")
for i in sayilar:
    if (i % 3 == 0):
        print(i)
print()

# 2) Sayilar listesinde sayıların toplamı kaçtır ?
print("Soru 2")
toplam = 0
for i in sayilar:
    toplam += i
    print("Toplam: ",toplam)
print()

# 3) Sayilar listesindeki tek sayıların karesini alınız.
for i in sayilar:
    if (i % 2 == 1):
        print(i**2)
print()

sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?
print("Soru 4")
for sehir in sehirler:
    print(len(sehir) <= 5)   # len = uzunluk demek yani elemanların toplamını verir
    print(sehir)
print()

urunler = [
    {'name':'samsung S6', 'price': '3000' },
    {'name':'samsung S7', 'price': '4000' },
    {'name':'samsung S8', 'price': '5000' },
    {'name':'samsung S9', 'price': '6000' },
    {'name':'samsung S10', 'price': '7000' }
]

# 5) Ürünlerin fiyatları toplamı nedir ?
print("Soru 5")
toplam = 0
for urun in urunler:
    fiyat = int(urun["price"])
    toplam += fiyat
print("Toplam ürün fiyatı: " , toplam)
print()

# 6) Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?
print("Soru 7")
for urun in urunler:
    if (int(urun["price"]) <= 5000):
        print(urun["name"])
