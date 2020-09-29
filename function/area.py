def geron (a,b,c):
    p=(a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**0.5
    return s

def length(x1,x2,y1,y2):
    p=(((x1-x2)**2)+((y1-y2)**2))**0.5
    return p

ax=int(input("х точки А: "))
ay=int(input("y Точки А: "))
bx=int(input("х точки B: "))
by=int(input("y Точки B: "))
cx=int(input("х точки C: "))
cy=int(input("y Точки C: "))
dx=int(input("х точки D: "))
dy=int(input("y Точки D: "))

ab=length(ax,bx,ay,by)
print(ab,"-сторона AB ")

bc=length(bx,cx,by,cy)
print(bc,"-сторона BC ")

cd=length(cx,dx,cy,dy)
print(cd,"-сторона CD ")

da=length(dx,ax,dy,ay)
print(da,"-сторона DA ")

ac=length(ax,cx,ay,cy)
print(ac)

P=ab+bc+cd+da
print(P,"-периметр")
p=(ab+bc+cd+da)/2
s=((p-ab)*(p-bc)*(p-cd)*(p-da))**0.5
print(s,"-Площадь")

abc=geron(ab,bc,ac)
acd=geron(ac,cd,da)
print(abc+acd,"-Площадь")