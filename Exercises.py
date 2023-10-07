from random import randint

"""secim = input("Sayı girin: ")

def bes_bastir():
    print(5)

if secim == "bes":
    bes_bastir()
"""


# *********************************************************

"""kisa_kenar = int(input("KISA KENAR: "))
uzun_kenar = int(input("UZUN KENAR: "))

alan = kisa_kenar*uzun_kenar
cevre = (kisa_kenar+uzun_kenar)*2

print("ALAN: {}".format(alan) + "\nÇEVRE: {}".format(cevre))
"""

# *********************************************************
#Python Example showing the sum of the numbers between two user-entered numbers.
"""num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
sum = 0

for i in range(num1+1,num2):
    sum+=i
print("SUM: {}".format(sum))
"""
# *********************************************************
#Calculating the area of a circle with a radius using a function.

"""rad = int(input("Radius: "))

def area(r):
    return 3.14*r*r

print(area(rad))
"""

# *********************************************************

#Python example calculating the area of a rectangle whose width and height are entered using a function.

"""kisa = int(input("KISA KENAR: "))
uzun = int(input("UZUN KENAR: "))

def alan(k,u):
    return k*u

print("ALAN: ", alan(kisa,uzun))
"""

# *********************************************************

"""random = randint(1,3)

while True:
    sayi = int(input("Sayı Gir:"))
    if sayi == random:
        print("BİLDİN!")
        break
    else:
        sayi = int(input("Sayı Gir:"))
        """

# *********************************************************

"""liste = [18,22,15,85,65,30,10,20,32,34,28,101,5,4,32]
sayac = 0
for i in liste:
    if i%5==0:
        sayac+=1
        print(i)
    else:
        pass
print("Toplam Sayı Adedi: {}".format(sayac))
"""

# *********************************************************

# Python example to find the average of even numbers between 2 numbers entered by the user.
# Whether the number is even or not is checked with the function.

num1 = int(input("NUM1: "))
num2 = int(input("NUM2: "))
sum = 0
count = 0

for i in range(num1,num2):
    if i%2==0:
        count+=1
        sum+=i

print(sum/count)



