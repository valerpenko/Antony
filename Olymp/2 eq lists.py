s=[1,3,4,6]#I
s1=[4,6,3,1]#i
I=0
i=0
while i !=len(s):
    if s[I]==s1[i]:
        i=0
        I+=1

print(I,i)