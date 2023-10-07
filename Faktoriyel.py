sayi = int(input("Sayı: "))
i = 0
f = 1
while i<sayi:
    i+=1
    f = i*f
print("{}! = ".format(sayi) + "{}".format(f))
