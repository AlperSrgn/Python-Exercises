kullanici1 = {
    'ad' : 'Ferhat',
    'soyad' : 'Yılmaz',
    'Uzmanlik' : ['Front-End']
}
kullanici2 = {
    'ad' : 'Burak',
    'soyad' : 'Güney',
    'Uzmanlik' : ['Tasarım']
}

kullanici3 = {
    'ad' : 'Mesut',
    'soyad' : 'Gün',
    'Uzmanlik' : ['Front-End']
}

print(kullanici1.get('Uzmanlik'))
print("*********************************")

kullanici_listesi = [kullanici1 , kullanici2 , kullanici3]

for i in kullanici_listesi:
    if i.get('Uzmanlik') == ['Front-End']:
        print(i.get('ad'))

print("*********************************")
kullanici3.get('Uzmanlik').append('Yazilim')
print(kullanici3.values())

print("*********************************")

for j in kullanici_listesi:
    if len(j['Uzmanlik']) > 1:
        print(j)

print("*********************************")

kullanici_yas_listesi = [22,34,32]
for j,k in zip(kullanici_listesi,kullanici_yas_listesi):
    if k < 30:
        print(j)

print("*********************************")

deger = 12
x = deger-1

while x>1:
    if deger%x==0:
        print("asal değil")
        break
    else:
        x-=1
else:
    print("asal")

