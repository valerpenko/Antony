#import math
fact=1
n=int(input())
i=1
while i<n+1:
    fact=fact*i
    i+=1
print(fact)

haz7 = False
while f>0:
    digit=f%10 #при помещении эого цикла в вайл происходит сбой n переменной
    f=f//10

    if digit ==7:
        haz7=True
        break

if haz7==False:
    print("Нет")
else:
    print("Да")
