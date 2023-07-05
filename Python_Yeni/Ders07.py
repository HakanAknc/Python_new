message = "Hello There. My name is Hakan Akıncı"
print(message)
print()

message = message.upper()         # Bütün harfleri BÜYÜK harfe çevirir
print(message)
print()

message = message.lower()         # Bütün harfleri KÜÇÜK harfe çevirir
print(message)
print()

message = message.title()         # Her kelimenin BAŞ harfini BÜYÜK yazar
print(message)
print()

message = message.capitalize()    # Sadece İLK kelimeyi BÜYÜK yazar diğerleri küçük
print(message)
print()

message = message.strip()         # BOŞLUK karekterlerini siler
print(message)
print()

message = message.split()         # Her kelimeyi ayırır
print(message)
print()
print(message[0])    # 0.indisi yazar
print(message[2])    # 2.indisi yazar

message = "---".join(message)     # Aralara istediğmizi koyabilirz
print(message)
print()

index = message.find('Hakan')     # Bulunan ilk indeks'ten keser
print(index)
print()

isFound = message.startswith('H') # Yazılan mesaj hangi harfle başlıyor
print(isFound)

isFon = message.endswith('n')     # Yazılan mesaj hangi harfle bitiyor
print(isFon)
print()

message = message.replace('Hakan','Evren')   # Hakan yerine Evren ismini yazıyor
print(message)
print()

message = message.replace('ç','c').replace('ö','o').replace(' ','-')
print(message)
print()

message = message.center(50,'*')  # Sağında ve solunda 50cm lik boşluklar bırakır
print(message)
print()

