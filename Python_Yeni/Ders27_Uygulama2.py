
# 1) Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
print("Soru 1")
sayi = float(input("Sayı girin: "))

if (sayi > 0) and (sayi <= 100):
    print("Sayı 0-100 arasında")
else:
    print("Sayı 0-100 arasında değil")
print()


# 2) Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
print("Soru 2")
sayi2 = int(input("Sayı girin: "))

if (sayi2 > 0):
    if (sayi2 % 2 == 0):
        print("Sayı pozitif çift sayıdır")
    else:
        print("Sayı tektir")
else:
    print("Sayı negatiftir ")
print()


# 3) Email ve parola bilgileri ile giriş kontrolü yapınız.
print("Soru 4")
email = "hakanakinci"
parola = "1234"

girilenemail = input("email girin: ")
girilenparola = input("parola girin: ")

if (girilenemail == email):
    if (girilenparola == parola):
        print("Giriş başarılı HOŞGELDİNİZ :)")
    else:
        print("Parola hatalı ):")
else:
    print("email hatalı")
print()


# 4) Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
print("Soru 4")
x = int(input("X: "))
y = int(input("Y: "))
z = int(input("Z: "))

if (x > y) and (x > z):
    print("x büyüktür")
elif (y > x) and (y > z):
    print("y büyüktür")
else:
    print("z büyüktür")
print()


# 5) Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#   a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#   b-) Finalden 70 alındığında ortalamanın önemi olmasın.
print("Soru 5")
vize1 = int(input("1.Vize notunu girin: "))
vize2 = int(input("2.Vize notunu girin: "))
final = int(input("Final notunu girin: "))

ortalama = (((vize1 + vize2)/2)*0.6) + (final*0.4)

result = (ortalama >= 50) and (final >= 50)
result = (ortalama >= 50) or (final >= 70)

# 1.durum
if (ortalama >= 50):
    if (final >= 50):
        print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: Başarılı')
    else:
        print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: Başarısız. Finalden en az 50 almalısınız.')
else:
    print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: Başarısız')

# 2.durum
if (ortalama >= 50):
    print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı')
    if (final >= 70):
        print(
            f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı. Finalden en az 70 aldığınız için geçtiniz.')
    else:
        print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız')
print()


# 6) Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
   # Formül: (Kilo / boy uzunluğunun karesi)
   # Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
   # 0-18.4    => Zayıf
   # 18.5-24.9 => Normal
   # 25.0-29.9 => Fazla Kilolu
   # 30.0-34.9 => Şişman (Obez)
print("Soru 6")
name = input('Adınız: ')
kg = float(input('Kilonuz: '))
hg = float(input('Boyunuz: '))
index = (kg) / (hg ** 2)
if (index >= 0) and (index<=18.4):
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf.')
elif (index>18.4) and (index<=24.9):
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal.')
elif (index>24.9) and (index<=29.9):
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu.')
elif (index>=29.9) and (index<=45.9):
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez.')
else:
    print('bilgileriniz yanlış.')


