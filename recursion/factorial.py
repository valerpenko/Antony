def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
for i in range (1,30):
    F=fact(i)
    print(F, end='\t')
    P=10 ** i
    print(P)
    if F>P:
        print ("i=",i)
        break
for i in range (1,fact(30)):
    pass
print("Happy end!")





