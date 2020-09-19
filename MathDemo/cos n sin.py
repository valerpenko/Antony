import math
for i in range(0,181,1):
    r=math.radians(i)
    s=math.sin(r)
    c=math.cos(r)
    if math.fabs(s-c)<0.01:
        print(i)
        break

i=0
r = math.radians(i)
s = math.sin(r)
c = math.cos(r)
while math.fabs(s-c)>0.01:
    i += 1
    r = math.radians(i)
    s = math.sin(r)
    c = math.cos(r)
print(i)






