website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
result1 = len(course)     # coursa dizi uzunluğu
length = len(website)    # website dizi uzunluğu
print(result1)
print(length)
print()

# 2- 'website' içinden www karakterlerini alın.
result2 = website[7:10]
print(result2)
print()

# 3- 'website' içinden com karakterlerini alın.
result3 = website[22:25]
result4 = website[length-3:length]
print(result3)
print()

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
result5 = course[0:15]
result6 = course[:15]
result7 = course[-15:]
print(result5)
print()

# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
result8 = course[::-1]
print(result8)
print()

name, surname, age, job = 'Hakan','AKINCI', 21, 'Yazıl Mühendisi'

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Hakan AKINCI, Yaşım 21 ve mesleğim mühendis.'

result9 = "Benim adım "+ name+ " " + surname+ ", Yaşım "+ str(age) + " ve Mesleğim "+ job
result10 = "Benim adım {0} {1}, Yaşım {2} ve Mesleğim {3}.".format(name,surname,age,job)
result11 = f'Benim adım {name} {surname}, Yaşım {age} ve "Mesleğim" {job}.'
print(result9)
print()

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s = 'Hello world'
s = s[0:6] + 'W'+ s[-4:]
print(s)
print()

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
result12 = 'abc ' * 3
print(result12)
print()

