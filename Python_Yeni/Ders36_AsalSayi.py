"""
Soru: Girilen bir sayının asal olup olmadığını bulun.
** Asal Sayı 1 ve kendisi hariç tam böleni olmayan
   sayılara denir.
"""

sayi = int(input("Sayı: "))
asalMi = True

if sayi == 1:
    asalMi = False

for i in range(2,sayi):
    if sayi % i == 0:
        asalMi = False

if asalMi:
    print("Sayı asaldır.")
else:
    print("Sayı asal değildir")