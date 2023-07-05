# break ve continue ifadeleri
# break komutu döngüyü sonlandırır,
# continue ise döngünün o turunu sonlandırır ve bir sonraki turdan devam eder.


name = 'Hakan Akıncı'

print("continu ile çözüldü")
for letter in name:
     if letter == 'n':
         continue
     print(letter)
print()

print("break ile çözüldü")
for letter in name:
     if letter == 'n':
         break
     print(letter)
print()


x = 0

while x < 5:    
     x+=1
     if x == 2:
         continue   # 2'yi atlar devam eder break olsa 2'den sonrasını yazmaz
     print(x)
print()


# 1- 100 e kadar tek sayıların toplamı

x = 0
result = 0

while x <= 100:    
    x+=1
    if x % 2 == 0:
        continue
    result += x

print(f'toplam: {result}')

