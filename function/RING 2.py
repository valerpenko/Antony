p=3.14
R=int(input("Радиус большой окр"))
r=R-1 #радиус мальенькой окр
s=(r**2)*p
S=(R**2)*p-s
i=1
print(S,s,r,i)
while s>S:
    r-=i
    s = (r ** 2) * p
    S = (R ** 2) * p - s
    print(S, s, r, i)

i=1*(-0.1)
while s<S:
    r-=i
    s = (r ** 2) * p
    S = (R ** 2) * p - s
    print(S, s, r, i)
i=1*(-0.01)
while s>S:
    r-=i
    s = (r ** 2) * p
    S = (R ** 2) * p - s
    print(S, s, r, i)




