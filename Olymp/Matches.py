n=int(input())
i=2
restCubes=0
if n>2 and (n**0.5)%1==0: #1 этап
    Im=n**0.5
    Im=(Im*4)+(Im-1)*Im*2
else:
    while i**2<n:   #2 этап если
        i+=1
    i=i-1
    i=i**2
    restCubes=n-i

    Im=i**0.5
    Im=(Im*4)+(Im-1)*Im*2

    if i**0.5<restCubes:
        Im=Im+(3*2)+2*(restCubes-2)
    else:
        Im=Im+3+2*(restCubes-1)
print(round(Im))