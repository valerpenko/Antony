l=5
print(l)
l=[3,5,7,2,7]
print(l)
print(l*2)
for element12 in l:
    if element12!=l[len(l)-1]:
        print(element12 * 2, end=', ')
    else:
        print(element12 * 2)


