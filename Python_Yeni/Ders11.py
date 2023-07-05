numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val1 = min(numbers)
val2 = max(numbers)
val3 = min(letters)
val4 = max(letters)
print(val1)
print(val2)
print(val3)
print(val4)
print()

val5 = numbers[3:6]
val6 = numbers[:3]
print(val5)
print(val6)
print()

numbers[4] = 40
print(numbers)
print()

numbers.append(49)      # diziye eleman ekler
numbers.append(59)
numbers.insert(3, 78)   # istediğn yere eleman ekler
numbers.insert(-1, 52)  # istediğn yere eleman ekler
print(numbers)
print()

numbers.pop()    # dizideki elemanı siler
numbers.pop(0)   # dizideki elemanı siler
numbers.pop(-1)
numbers.remove(49)    # istenilen elemanı siler
print(numbers)

numbers.sort()   # bütün elemanları sıralar
print(numbers)
letters.sort()
print(letters)
print()

numbers.reverse()   # listeyi tam tersine çeviri
print(numbers)
print()

print(len(numbers))   # eleman sayısını verir
print(len(letters))
print()

print(numbers.count(10))   # 10 elemanı numbers'de kaç kere var
print(letters.count("a"))  # a elemanı letters'de kaç kere var
print()

numbers.clear()    # diziyi temizler
print(numbers)
print()