# key - value
# 07 => Antalya , 34 => İstanbul

# Liste ile çözüm
sehirler = ["Antalya","İstanbul"]
plakalar = [7, 34]
print(plakalar[sehirler.index("Antalya")])
print(plakalar[sehirler.index("İstanbul")])
print()

# Dictionary ile çözüm
# print(plakalar['kocaeli']) => 41
# print(plakalar['istanbul']) => 34

plakalar = {"Antalya" : 7, "İstanbul" : 34}
print(plakalar["Antalya"])
print(plakalar["İstanbul"])

plakalar["Siirt"] = 56
print(plakalar)
plakalar["Antlaya"] = "Kumluca BAŞKENT"
print(plakalar)
print()

users = {
    "hakanakinci": {
        "yas": 21,
        "gmail": "hakan@gmail.com",
        "telefon": "5425435636"
    },
    "evrenakinci": {
        "yas": 8,
        "gmail": "evren@gmail.com",
        "telefon": "5372559466"
    }
}
print(users["hakanakinci"])
print(users["hakanakinci"]["yas"])
print(users["hakanakinci"]["gmail"])
print(users["hakanakinci"]["telefon"])
print()

print(users["evrenakinci"])
print()

#Örnek 2
ogrenci = {
  "numara": "120",
  "ad": "Ahmet",
  "soyad": "Yılmaz"
}

numara = ogrenci.get("numara")
ad = ogrenci.get("ad")
soyad = ogrenci.get("soyad")

print(numara,ad,soyad)  # 120 Ahmet Yılmaz
