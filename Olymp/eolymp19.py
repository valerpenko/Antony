#Степень симметрии
import math
n=input()
k=0
for i in range(0,len(n)//2+1):
    if n[i]==n[len(n)-1-i]:
        k+=1
print(k)
