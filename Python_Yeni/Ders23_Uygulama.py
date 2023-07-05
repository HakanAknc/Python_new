
# 1) Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
print("Soru 1")
sayi = float(input("Sayı giriniz: "))
sonuc = (sayi > 0 and sayi < 100)
print(f"Sayı 0-100 arasında: {sonuc}")
print()


# 2) Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
print("Soru 2")
sayi1 = int(input("Sayı giriniz: "))
ciftpoz = (sayi1 > 0) and (sayi1 % 2 == 0)
print(f'Girilen sayı pozitif çift sayı mı: {ciftpoz}')
print()


# 3) E-mail ve parola bilgileri ile giriş kontrolü yapınız.
print("Soru 3")
email = "hakanakinci"
parola = "12345"

girilenEmail = input("e_mail girin: ")
girilenparola = input("parola girin: ")

giris = (email == girilenEmail) and (parola == girilenparola)
print(f'Uygulamaya giriş başarılı mı: {giris}')
print()


# 4) Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
print("Soru 4")
a = float(input("a sayısı: "))
b = float(input("b sayısı: "))
c = float(input("c sayısı: "))

buyuk = (a>b) and (a>c)
print(f"a en büyük sayıdır: {buyuk}")

buyuk = (b>a) and (b>c)
print(f"b en büyük sayıdır: {buyuk}")

buyuk = (c>a) and (c>b)
print(f"c en büyük sayıdır: {buyuk}")
print()


# 5) Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

print("Soru 5")
vize1 = float(input("Vize1 notu: "))
vize2 = float(input("Vize2 notu: "))
final = float(input("Final notu: "))

ortalama = (((vize1 + vize2)/2)*0.6) + (final * 0.4)
result = (ortalama>=50) and (final>=50)
result = (ortalama>=50) or (final>=70)
print(f"Öğrencinin ortalaması: {ortalama} \nGeçme dururmu: {result}")
print()


# 6) Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf
#    18.5-24.9 => Normal
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)
print("Soru 6")
ad = input("İsim gir: ")
kilo = float(input("Kilo gir: "))
boy = float(input("Boy gir: "))

formul = (kilo) / (boy ** 2)

zayif = (formul >= 0) and (formul <= 18.4)
normal = (formul > 18.4) and (formul <= 24.9)
kilolu = (formul > 24.9) and (formul <= 29.9)
obez = (formul >= 29.9) and (formul <= 34.9)

print(f'{ad} kilo indeksin: {formul} ve kilo değerlendirmen zayıf: {zayif}')
print(f'{ad} kilo indeksin: {formul} ve kilo değerlendirmen normal: {normal}')
print(f'{ad} kilo indeksin: {formul} ve kilo değerlendirmen kilolu: {kilolu}')
print(f'{ad} kilo indeksin: {formul} ve kilo değerlendirmen obez: {obez}')

