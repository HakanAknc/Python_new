# 5.bölüm  python koşul ifadeleri

print("Soru 1")
username = "hakanakinci"
password = "1234"

if (username == "hakanakinci"):
    if (password == "1234"):
        print("Hoşgeldiniz :)")
    else:
        print("password yanlış ):")
else:
    print("username yanlış")
print()


print("Soru 2")
x = int(input("sayı gir: "))
y = int(input("sayı gir: "))

if (x > y):
    print("x sayısı büyüktür.")
elif (x == y):
    print("x = y eşittir")
else:
    print("y sayısı büyüktür")
print()


print("Soru 3")
num = int(input("Sayı girin: "))

if (num > 0):
    print("Sayı pozitiftir")
elif (num < 0):
    print("Sayı negatiftir")
else:
    print("Sayı sıfırdır")
