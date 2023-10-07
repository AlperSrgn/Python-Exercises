# ÇOK BOYUTLU VERİ TİPLERİ (DİCTİONARY)

dict1 = {
    "isim": "alper",
    "yaş": 20,
    "lokasyon": {
        "dogdugu_sehir": "istanbul",
        "yasadigi_sehir": "Ankara"
    }
}

print(dict1["isim"])
print(dict1.get("yaş"))
print(dict1.keys()) # keyleri yazdırır
print(dict1.values()) # keylerin karşısındaki değerleri yazdırır
print(dict1.items()) # keyleri ve karşısındaki değerleri yazdırır
print(dict1["lokasyon"])

print()
#########################################################################################################################################

# KOLEKSİYON VERİ TİPLERİ (LİST VE SET)

harf = ['g','h','j','k','l']
harf.append('f') # eleman ekler
harf.remove('h') # h elemanını siler
harf.pop(2) # 2. indexteki elemanı siler. içi boş olursa en sondaki elemanı siler.
print(harf[3:5])
print(harf)

sayilar = ["132","1","321","1","789","654"]
sayilar.sort() # küçükten büyüğe sıralar
sayilar.reverse()
print(sayilar)
print(set(sayilar)) # 'set' komutu, aynı olan elemanları bir defa yazar


print()
#########################################################################################################################################

# SABİT KOLEKSİYON VERİ TİPİ (TUPLE)

liste = ['a','b','c','d','e']
print(liste)
tup = ('a','b','c','d','e')   # TUPLE TİPİ OBJELERİN ELEMANLARI DEĞİŞTİRİLEMEZ
print(tup)

liste[0] = '123'
print(liste)

print(tup.count('t')) # listede kaç tane bu elemandan var
print(tup.index('c')) # elemanın kaçıncı indexte olduğu

