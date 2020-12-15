def sum(a):
    if len(a)==0:
        return(0)
    if len(a)==1:
        return a[0]

    b=a[:len(a)//2]
    c=a[len(a)//2:]
    return sum(b)+sum(c)
a=[6,6,6,6]
print(sum(a))