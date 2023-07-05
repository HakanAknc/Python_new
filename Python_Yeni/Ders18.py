# Atama Operatörleri

# x = 5
# y = 10
# z = 20

# x, y, z = 5, 16, 20
# print(x,y,z)

# x, y = y, x
# print(x,y)

# x += 5          # x = x + 5
# x -= 5          # x = x - 5
# x *= 5          # x = x * 5
# x /= 5          # x = x / 5
# x %= 5          # x = x % 5
# y //= 5         # y = y // 5
# y **= z         # y = y ** z


values = 1, 2, 3, 4, 5

print(values)
print(type(values))

x, y, *z = values  # x=1,y=2,z=3,4,5 elemanlarına gider

print(x, y, z)
print(x, y, z[1])