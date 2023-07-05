# Yöntem 1
# import math
# import math as islem

# value = dir(math)              // kullana bileceğmiz işlemleri gösterir
# value = help(math)            // kullanılabilecek math kütüphanelerini açıklar
# value = help(math.factorial) //nasıl kullanıldığını açıklar
# value = math.sqrt(49)       //karekök alır
# value = math.factorial(5)  // faktöriyeli hesaplar
# value = math.floor(5.9)   // aşağı yuvarlar
# value = math.ceil(5.9)   // yukarı yuvarlar

# value = islem.factorial(5)

# Yöntem 2
# from math import *    // Bütün fonksiyonları import ettik

def sqrt(x):
    print('x :'+ str(x))

from math import factorial,sqrt,ceil

# value = factorial(5)
value = sqrt(9)
# value = ceil(9.8)

print(value)