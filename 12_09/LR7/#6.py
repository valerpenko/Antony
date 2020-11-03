a=[9,4,3,2,7,1]
for i in range(1,len(a)):
    if a[i] >= a[i-1]:
        print(False)
        exit()
print(True)