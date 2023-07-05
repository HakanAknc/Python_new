# 1) Girilen 2 sayıdan hangisi büyüktür ?
print("Soru 1")
a = int(input("Sayı giriniz: "))
b = int(input("Sayı giriniz: "))
sonuc = (a > b)
print(f"a: {a} b: {b} den büyüktür {sonuc}")
print()


# 2) Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
print("Soru 2")
vize1 = float(input("Vize notu: "))
vize2 = float(input("Vize notu: "))
final = float(input("Final notu: "))

ortalama = (((vize1 + vize2)/2) * 0.6) + (final * 0.4)
print(f"Not ortalamanız: {ortalama} \nDersten geçme durumunuz: {ortalama>=50}")
print()


# 3) Girilen bir sayının tek mi çift mi olduğunu yazdırın.
print("Soru 3")
sayi = int(input("Sayı giriniz: "))
tekcift = sayi % 2 == 0
print(f"Girilen sayının çift olma dururmu: {tekcift}")
print()


# 4) Girilen bir sayının negatif pozitif durumunu yazdırın.
print("Soru 4")
sayi1 = int(input("Sayı giriniz: "))
negpoz = (sayi1 > 0)
print(f"Girilen sayının pozitif olma durumu: {negpoz}")
print()


# 5) Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: email@sadikturan.com parola:abc123)
print("Soru 5")
email = "hakanakinci"
password = "123abc"

girilenemail = input("e-mail: ")
girilenpassword = input("şifre: ")

isemail = (email == girilenemail.lower().strip())  #lower() = büyük küçük hatf uyumunu sağlar. strip() = boşlukları siler
ispassword = (password == girilenpassword.lower())   #lower() = büyük küçük hatf uyumunu sağlar

print(f"Email bilgisi doğrumu: {isemail} ve Parola doğrumu {ispassword}")








