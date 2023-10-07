# listelerde FOR döngüleri

liste = [[1, 2], [3, 4], [5, 6]]

for x, y in liste:
    print(x * y)

print()

kullanici = {
    "ad": "ali",
    "soyad": "yılmaz"
}

print(kullanici.items())
print(kullanici.keys())
print(kullanici.values())

for k in kullanici:
    print("key: {}".format(k))

print()

for k, v in kullanici.items():
    print("key: {} \t value: {}".format(k, v))

#########################################################################################################################################

sayi1 = 0
while sayi1<10:
    print("{} değeri 10 dan küçüktür".format(sayi1))
    sayi1 += 1

girilen_sayi = 5
sonuc = 1

while girilen_sayi > 0:
    sonuc = sonuc*girilen_sayi
    girilen_sayi-=1

print(sonuc)
