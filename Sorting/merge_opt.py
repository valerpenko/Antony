a=[1,5,10,12]
b=[2,3,8,13,14,15,16,17]
c=[]
ia=0
ib=0
while(ia<len(a) and ib<len(b)):
    if a[ia]>b[ib]:
        c.append(b[ib])
        ib+=1
    else:
        c.append(a[ia])
        ia+=1
if ia<len(a):
    for i in range(ia,len(a)):
        c.append(a[i])
else:
    for i in range(ib,len(b)):
        c.append(b[i])
print(c)
