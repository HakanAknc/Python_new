website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
result1 = ' Hello World '.strip()         # Boşluk karekterlerini siler
result2 = ' Hello World '.lstrip()        # SAĞdaki boşlıkları siler
result3 = ' Hello World '.rstrip()        # SOLdaki boşlıkları siler
print(result1)
print(result2)
print(result3)

result4 = website.lstrip('/:pth')
print(result4)
print()

# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
result5 = 'www.sadikturan.com'.strip('w.moc')    # Boşluk karekterlerini siler
print(result5)

# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
result6 = course.lower()           # Tüm karekterleri küçük harfe çevirir
result7 = course.upper()           # Tüm karekterleri büyük harfe çevirir
result8 = course.title()           # Sadece baş harfler büyük harfe çevirir
print(result6)
print(result7)
print(result8)
print()

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
result9 = website.count('a')
result10 = website.count('www')
result11 = website.count('www',0,10)     # 0 ile 10 indisleri arasında www harflerini ara
print(result9)
print(result10)
print(result11)
print()

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
result12 = website.startswith('www')     
result13 = website.startswith('http')
result14 = website.endswith('com')
print(result12)
print(result13)
print(result14)
print()

# 6-  'website' içinde '.com' ifadesi var mı?
result15 = website.find('com')
result16 = website.find('com',0,10)
result17 = course.find('Python')
result18 = course.rfind('Python')
print(result15)
print(result16)
print(result17)
print(result18)
print()

result19 = website.index('com')
result20 = website.rindex('com')
print(result19)
print(result20)
print()
# result = website.rindex('comm') # exception

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
result21 = course.isalpha()
result22 = 'Hello'.isalpha()
result23 = course.isdigit()
result24 = '123'.isdigit()
print(result21)
print(result22)
print(result23)
print(result24)
print()

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result25 = 'Contents'.center(50, '*')
result26 = 'Contents'.ljust(50, '*')
result27 = 'Contents'.rjust(50, '*')
print(result25)
print(result26)
print(result27)
print()

# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
result28 = course.replace(' ', '-')
result29 = course.replace(' ', '-',5)
result30 = course.replace(' ', '')
print(result28)
print(result29)
print(result30)
print()

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
result31 = 'Hello World'.replace('World','There')
print(result31)
print()

# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.
result32 = course.split(' ')
print(result32)
# result = result[2]
result33 = result32[5]
print(result33)

