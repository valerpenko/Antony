l=[3,1,7,5,8,11,4]
b=5
l=[3,1,5,4,    8,11,7]
l1=[]
i=0
while i<len(l):
    if l[i]>=b:
        l1.append(l.pop(i))
    else:
        i+=1
print(l)
print(l1)
l.extend(l1)
print(l)
