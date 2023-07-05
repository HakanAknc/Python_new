# 0 - 100'e kadar

x = 1
while x < 10:
    if x % 2 == 1:
        print(f"{x} : tek sayı")
    else:
        print(f"{x} : çift sayı")
    x = x + 1
print("bitti...")
print()

name = '' # False
while not name.strip():    #not name.strip():
    name = input('isminizi giriniz: ')

print(f'Merhaba, {name}')

