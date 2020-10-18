a=int(input())
b=int(input())
r0=0
while r0!=1:
    q0=a//b
    print (q0)
    r0=a%b
    a=b
    b=r0
print(a)

