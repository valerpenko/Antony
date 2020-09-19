x=int(input())

sum=0
while x != 0:
    y = x % 10
    x = x // 10
    if y%2==0:
        #print(y)
        sum+=y
print(sum)





