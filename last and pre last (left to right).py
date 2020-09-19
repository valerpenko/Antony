x1=int(input(""))
x=x1
i=0
while x != 0:
    y = x % 100
    if y % 11 == 0:
        i+=1
    x = x // 100
print(i)

x=x1
i=0
while x != 0:
    d1 = x % 10
    x=x//10
    d2 = x % 10
    if d1 ==d2:
        i+=1
    x = x // 10
print(i)