c=int(input())
d=int(input())
a=int(input())
b=int(input())
print('\t')
for i in range(a,b+1):
    print(i,"\t",end='')
print()
for j in range(c,d+1):
    print(j,'\t',end='')
    for k in range(a,b+1):
        print(j*k,"\t",end='')
    print()

