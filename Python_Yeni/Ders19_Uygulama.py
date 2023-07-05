x,y,z = 2,5,10

# 1) Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir ?
a = int(input("Sayı girinzi: "))
b = int(input("Sayı giriniz: "))
sonuc = (a*b) - (x+y+z)
print(sonuc)
print()

# 2-) y'nin x'e kalansız bölümünü hesaplayınız.
bolum = y // x
print(bolum)
print()

# 3) (x,y,z) toplamının mod 3' ü nedir ?
toplam = (x+y+z)
mod = toplam % 3
print(mod)
print()

# 4) y'nin x.kuvvetini hesaplayınız.
kuvvet = y ** x
print(kuvvet)
print()

# 5-) x, *y, z = numbers işlemine göre z' nin küpü kaçtır ?
numbers =1,5,7,10,6
x, *y, z = numbers
kup = z ** 3
print(kup)
print()

# 6) x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır ?
numbers = 1, 5, 7, 10, 6
x, *y, z = numbers

indis = y[0] + y[1] + y[2]    # y'nin indisleri y (5,7,10)
print(indis)
