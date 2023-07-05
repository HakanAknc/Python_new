def changeName(n):
    n = "Ada"

name = "Yiğit"

changeName(name)
print(name)
print()


def change(n):
    n[0] = "İstanbul"

sehirler = ["ankara","izmir"]
change(sehirler)
print(sehirler)
print()


def add(a,b,c = 0):
    return sum((a,b,c))
print(add(30,15))
print(add(30,15,15))
print()


def add(*params):
    print(type(params))
    sum = 0
    for n in params:
        sum = sum + n
    return sum

print(add(10, 20, 50))
print(add(10, 20, 30))
print(add(10, 20, 30,50,60,10,20))
print()

