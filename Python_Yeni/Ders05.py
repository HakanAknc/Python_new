name = "Hakan"
surname = "Akıncı"
age = 21

"""
greeting = "My name is " + name + " "+ surname + " and \nI am " + str(age) + " years old"
print(greeting)
print()
print(greeting[0])         # indis 0
print(greeting[3])         # indis 3
print(len(greeting))       # indis uzunluğunu verir
print(greeting[-1])        # son indisi alır
print(greeting[3:7])       # 3.indisten 7.indise kadar olanları alır
print(greeting[3:])        # 3.indisten başla sona kadar
print(greeting[:16])       # en baştan başlar 15.indiste durur
print(greeting[2:40:2])    # 2.indisten başla 40'a kadar ikişer ikişer yazdır
"""

ad = "Hakan"
soyad = "Akıncı"
yas = 21

#print("My name is {} {}".format(name, surname))
#print("My name is {1} {0}".format(name, surname))
#print("My name is {s} {n}".format(n=name, s=surname))
#print("My name is {} {} and I'm {} old years".format(name, surname, yas))

# f string
print(f"My name is {ad} {soyad} and I'm {yas} old years")


