# value types => string, number
# value types ile ilgilenirken verinin kendisiyle ilgilenirz.
x = 5
y = 25

x = y

y = 10

print(x,y)

# print(x,y)

# reference types => list
# reference types ile ilgilenirken de listenin adresiyle ilgileniriz.
a = ["apple","banana"]
b = ["apple","banana"]

a = b

b[0] = "grape"

print(a, b)
