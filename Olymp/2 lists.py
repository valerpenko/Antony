a=[1,7,10]
b=[2,3,4]
c=a+b
d=[]
I=0
while I<(len(c)):
    place = 0
    i = 0
    while i<(len(c)):
        if c[I]>c[i]:
            place+=1
        i+=1
    I+=1
    print(place,c[I])