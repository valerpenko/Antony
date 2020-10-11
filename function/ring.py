p=3.14
R=int(input("Радиус большой окр"))
r=R-1 #радиус мальенькой окр
s=(r**2)*p
S=(R**2)*p-s
i=0.01
print(S,s,r,i)

while S<s:
    r-=i
    s = (r ** 2) * p
    S = (R ** 2) * p - s
    s=s//1
    S=S//1
    print(S, s, r, i)