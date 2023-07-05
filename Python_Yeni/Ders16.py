fruits = {"portakal", "elma", "muz"}
print(fruits)
print()

#print(fruits[0]) indekslenemez

for i in fruits:
    print(i)
print()

fruits.add("erik")   #ekler
print(fruits)

fruits.update(["mango","üzüm"])  #ekler
print(fruits)
print()

fruits.remove("mango")  #siler
print(fruits)
print()

fruits.clear()  # temizler
print(fruits)
print()

myList = [1,2,5,4,4,2,1]
print(myList)
print(set(myList))   # tekrarlanan elemanlar listeden çıkartılır