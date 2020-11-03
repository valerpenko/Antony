a=[12,-14,16]
b=[13,-19,20]
c=[2,-3,4]
i=0
while c[i]>=0 and a[i]>=0 and b[i]>=0:
    i+=1
if c[i]>=0:
    print(False)
else:
    if a[i]<0 or b[i]<0:
        print(False)
    else:
        print(True)