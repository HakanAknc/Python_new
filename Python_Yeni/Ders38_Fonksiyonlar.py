def seyHello(name):
    return "Hello " + name

msg = seyHello("Hakan")
print(msg)
print()


def totel(num1 , num2):
    return num1 + num2
toplam = totel(10,20)
print(toplam)
print()


def yasHesapla(dogumyili):
    return 2020 - dogumyili

yasCaner = yasHesapla(2004)
yasEyup = yasHesapla(2011)
yasEvren = yasHesapla(2018)

print(yasCaner , yasEyup ,yasEvren)
print()


# Emeklilik hesaplama sorusu

def EmekliligeKacYilKaldi(dogumYili , isim):
    """"
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldı
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    """
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f"Emekliliğinize {emeklilik} yıl kaldı")
    else:
        print("Zaten emekli oldunuz")

EmekliligeKacYilKaldi(1960, "Sercan")
EmekliligeKacYilKaldi(1955, "Özcan")
EmekliligeKacYilKaldi(1970, "Ercan")


