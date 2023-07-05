print("Python'a Hoşgeldiniz...")
print(2+2)
print(5000 - (5000 * 0.27))

maasAli = 5000
maasAhmet = 4500
vergi = 0.27

print(maasAli - (maasAli * vergi))
print(maasAhmet - (maasAhmet * vergi))

# Değişken tanımlama kuralları
# rakam ile başlayamaz

number1 = 10
print(number1)

number1 = 20
print(number1)

number1 += 30
print(number1)

# Büyük küçük harf duyarlılığı
# Değişken tanımlarken türkçe karekter kullanmayalım

x = 1                      # integer
y = 2.6                    # float
name = "Hakan"             # String
isStudent = True           # Boolean

a = '10'
b = '20'
print(a+b)  # a+b=30    =>   'a'+'b'=1020

# Tanımlanan değişkenkler arasında boşluk olamaz  = first Name (yanlış)
firstName = "Hakan"
lastName = " Akıncı"
print(firstName + lastName)