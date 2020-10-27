s=[1,3,5,8,6]#I
s1=[1,8,3,5]#i
I=0
i=0
res=0
while res<len(s):
    if s[I]==s1[i]:
        res+=1
        I+=1
        i=0
    else:
        i+=1
if res==len(s):
    print("Da")
else:
    print("Net")