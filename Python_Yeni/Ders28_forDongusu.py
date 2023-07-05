numbers = [1,2,3,4,5]
for num in numbers:
    print(num)
print()

names = ["Hakan","Caner","Eyüpcan","Evren"]
for name in names:
    print(name)
print()

name = "Yazılım"    # Tüm elemanları tek tek yazdırır
for a in name:
    print(a)
print()

tuple = [(1,2),(5,6),(7,8)]
for a,b in tuple:
    print(a,b)
print()

d = {'k1':1, 'k2':2, 'k3':3}

for key,value in d.items():   #dictionary
    print(key, value)