x = 5

hak = 0
devam = 'e'

result = 5 < x < 10

# and

# True, True => True
# True, False => False

result = (x > 5) and (x < 10)   # Her iki koşulun da sağlanması gerekşyor ===== AND
print(result)
result = (hak > 0) and (devam == 'e')
print(result)
print()

# or
result = (x > 0) or (x % 2 == 0)   # Sadece bir koşulun sağlanması yeterli ===== OR
print(result)

# True, False => True
# True, True => True
# False, False => False
print()

# not
result = not(x > 0)
print(result)

# x, 5-10 arasında olan bir çift sayı mı?

result = ((x>5) and (x<10)) and (x%2==0)
print(result)

