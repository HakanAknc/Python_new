# 1) "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
print("Soru 1 ")
arabalar = ["Bmw","Mercedes","Opel","Mazda"]
print(arabalar)
print()


# 2) Liste Kaç elemanlıdır. ?
print("Soru 2 ")
print(len(arabalar))
print()
#result = len(arabalar)


# 3) Listenin ilk ve son elemanı nedir.
print("Soru 3 ")
print(arabalar[0])
print(arabalar[3])
print(arabalar[-1])
print()
#print(arabalar[-1])  //son elemanı verir.


# 4) Mazda değerini Toyota ile değiştirin. ??
print("Soru 4 ")
arabalar[-1] = "Toyato"
print(arabalar)
print()


# 5) Listenin -2 indeksindeki değer nedir. ??
print("Soru 5 ")
print(arabalar[-2])
print()


# 6) Listenin ilk 3 elemanını alın. ??
print("Soru 6 ")
print(arabalar[0:3])
print(arabalar[:3])
print(arabalar[-2:])
print()


# 7) Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
print("Soru 7 ")
arabalar[-2:] = ["Toyato", "Renault"]
print(arabalar)
print()


# 8) Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
print("Soru 8 ")
arabalar = arabalar + ["Audi", "Nissan"]
print(arabalar)
print()


# 9) Listenin son elemanını silin.
print("Soru 9 ")
del arabalar[-1]
print(arabalar)
print()


# 10) Liste elemanlarını tersten yazdırınız.
print("Soru 10 ")
print(arabalar[::-1])   # Bütün listeyi al en sona git ve tersten yazdır
print(arabalar)
print()


# 11) Aşağıdaki verileri bir liste içinde saklayınız.

      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90)

print("Soru 11")
studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]
print(studentA)
print(studentB)
print(studentC)
print()


# 13) Liste elemanlarını ekrana yazdırınız.
print("Soru 12")
print(studentA[0])
print(studentB[1])
print(studentC[3][1])
yazdirma = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1] + studentA[3][2])/3}"
print(yazdirma)
print()


# 14) Mercedes listenin bir elemanı mıdır. ??
print("Soru 14")
arabalar = "Mercedes" in arabalar
print(arabalar)  #True
print()


