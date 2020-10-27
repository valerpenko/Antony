n=int(input())
i=2
d=0
if n>2 and (n**0.5)%1==0:
    I=n**0.5
    I=(I*4)+(I-1)*I*2
else:
    while i**2<n:
        i+=1
    i=i-1
    i=i**2
    d=n-i

    I=i**0.5
    I=(I*4)+(I-1)*I*2
    if i**0.5<d:
        I=I+(3*2)+2*(d-2)
    else:
        I=I+3+2*(d-1)
print(round(I))