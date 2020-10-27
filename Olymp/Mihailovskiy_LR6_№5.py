n=int(input())
if n>0:
    m=3
    res=1/1
    for i in range(2,n+1):
        res*=m/i
        m+=2
print(res)