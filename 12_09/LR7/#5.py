def digits(n):
    k=0
    while n>0:
        n=n//10
        k+=1
    return k
n=int(input())
s=0
for i in range(1,n+1):
    s=s+digits(i)/i**2
print(s)