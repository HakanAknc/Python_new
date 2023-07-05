list = [1,2,3,5]
tuple = 1,'iki',3

print(type(list))
print(type(tuple))
print()

print(list[2])
print(tuple[2])
print()

print(len(list))
print(len(tuple))
print()

list = ["Damla","Ayşe"]
tuple = "Ali","Veli","Veli"
print(list)
print(tuple)
print()

list[0] = "Ahmet"
#tuple[0] = "Hakan"  // tuple'de tek bir eleman üzerinde değişim yapmaya izin vermez
print(list)
print()

print(tuple.count("Veli"))   # listede kaç kere var
print(tuple.index("Veli"))
print()


