a=[1,3,5,7,3]
b=[7,3,1,4, 5]

res=0
for ia in range(0,len(a)):
    ib=0
    while (ib<len(b)) and (a[ia]!=b[ib]):
        ib+=1
    if ib<len(b):
        res+=1
if res==len(a):
    print("Yes")
else:
    print("No")

for elA  in a:
    for iB in range(len(b)):
        if elA==b[iB]:
            break
        else:
            if iB==len(b)-1:
                print("No")
                exit()
print("yes")

for elA  in a:
    if not (elA in b):
        print("No")
        exit()
print("yes")
