numbers = []
for x in range(10):
    numbers.append(x)

print(numbers)
print()

numbers = [x for x in range(10)]
print(numbers)
print()

for x in range(10):
    print(x**2)

numbers = [x**2 for x in range(10)]
print(numbers)

numbers = [x*x for x in range(10) if x%3==0]
print(numbers)
print()

myString = 'Hello'
myList = []

for letter in myString:
    myList.append(letter)
print(myList)

myList = [letter for letter in myString]
print(myList)
print()

years = [1983, 1999, 2008, 1956, 1986]
ages = [2019-year for year in years]
print(ages)
print()

results = [x if x%2==0 else 'TEK' for x in range(1, 10)]
print(results)
print()

result = []

for x in range(3):
    for y in range(3):
        result.append((x,y))

print(result)
print()

numbers = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers)