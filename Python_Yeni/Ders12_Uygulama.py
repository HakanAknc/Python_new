names = ['Ali','Yağmur','Hakan','Deniz']
years = [1999, 2000, 1998, 1987]

# 1) "Cenk" ismini listenin sonuna ekleyiniz.
print("Soru 1")
names.append("Cenk")   # append = Eklemek
print(names)
print()

# 2) "Sena" değerini listenin başına ekleyiniz.
print("Soru 2")
names.insert(0, "Sena")
# names.insert(-1, 'Mehmet')
# names.insert(len(names), 'Mehmet')
print(names)
print()

# 3) "Deniz" ismini listeden siliniz.
print("Soru 3")
names.remove("Deniz")
names.pop()
#names.pop(1) Ali'yi siler
print(names)
print()

# 4) "Hakan" isminin indeksi nedir ?
print("Soru 4")
index = names.index("Hakan")
names.pop(index)
print(index)
print()

# 5) "Ali" listenin bir elemanı mıdır ?
print("Soru 5")
result = "Ali" in names
result1 = names.index("Ali")
print(result)
print()

# 6) Liste elemanlarını ters çevirin.
print("Soru 6")
names.reverse()
print(names)
print()

# 7) Liste elemanlarını alfabetik olarak sıralayınız.
print("Soru 7")
names.sort()
print(names)
print()

# 8) years listesini rakamsal büyüklüğe göre sıralayınız.
print("Soru 8")
years.sort()
print(years)
print()

# 9) str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
print("Soru 9")
str = "Chevrolet,Dacia"
result2 = str.split(",")
print(result2)
print()

# 10) years dizisinin en büyük ve en küçük elemanı nedir ?
print("Soru 10")
min = min(years)
max = max(years)
print(min,max)
print()

# 11- years dizisinde kaç tane 1998 değeri vardır ?
print("Soru 11")
result3 = years.count(1998)
print(result3)
print()

# 12) years dizisinin tüm elemanlarını siliniz.
print("Soru 12")
years.clear()
print(years)
print()

# 13) Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
print("Soru 13")
markalar = []

marka = input("Marka: ")
markalar.append(marka)

marka = input("Marka: ")
markalar.append(marka)

marka = input("Marka: ")
markalar.append(marka)

print(markalar)
print()
