"""
   Daire Alanı = πr²
   Daire Çecresi = 2πr

   * Yarı çapı verilen bir dairenin alan ve çevrsini hesaplayanaz. (r: 3.14)
"""

pi = 3.14

r = float(input("Yarı çapı gir: "))

alan = pi * (r ** 2)
cevre = 2 * pi * r

print("Alan : " ,alan)
print("Çevre : " ,cevre)