print(range(10))        # [start:end]

print(list(range(5,20,2)))

print(*range(5,20,2))

for i in range(10):
    if i >5:
        print(i)
print()
#***************************************************************************************************************

harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

for harf in harfler:
    print(harf)

for harf in enumerate(harfler):     #index no
    print(harf)

print()
#***************************************************************************************************************

ulkeler = ['TR','FR','DE']
siraNo = range(1,4)

for i in zip(ulkeler,siraNo):
    print(i)

print()
#***************************************************************************************************************
harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

for index,harf in enumerate(harfler):
    if harf == 'e':
        print("{} harfi {}. indexte".format(harf,index))
        break

print()
#***************************************************************************************************************

for i in range(1,10):
    if i%2==0:
        pass
    else:
        print(i)

print()

for i in range(1,10):
    if i<5:
        pass
    else:
        print(i)





