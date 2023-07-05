ogrenciler = {
    "120": {
        "Ad": "Caner",
        "Soyad": "Akıncı",
        "Telefon": "123 456 78 94"
    },
    "125": {
        "Ad": "Eyüpcan",
        "Soyad": "Akıncı",
        "Telefon": "541 255 94 66"
    },
    "128": {
        "Ad": "Evren",
        "Soyad": "Akıncı",
        "Telefon": "101 234 56 96"
    },
}

      #1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
         #dictionary içinde saklayınız.

      #2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

ogrenciler1 = {}

number = input("Öğrenci no: ")
name = input("Öğrenci adı: ")
surname = input("Öğrenci soyadı: ")
phone = input("Öğrenci telefon: ")

ogrenciler1.update({
    number: {
        "Ad": name,
        "Soyad": surname,
        "Telefon": phone

    }
})
print()

number = input("Öğrenci no: ")
name = input("Öğrenci adı: ")
surname = input("Öğrenci soyadı: ")
phone = input("Öğrenci telefon: ")


ogrenciler1.update({
    number: {
        "Ad": name,
        "Soyad": surname,
        "Telefon": phone

    }
})
print()

number = input("Öğrenci no: ")
name = input("Öğrenci adı: ")
surname = input("Öğrenci soyadı: ")
phone = input("Öğrenci telefon: ")

ogrenciler1.update({
    number: {
        "Ad": name,
        "Soyad": surname,
        "Telefon": phone

    }
})
print()

# 2.soru
ogrNo = input("Öğrenci no: ")
ogrenci = ogrenciler1[ogrNo]
print(ogrenci)
print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['Ad']} soyadı: {ogrenci['Soyad']} ve telefonu ise {ogrenci['Telefon']}")