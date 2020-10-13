s='aaabbbddccc'
count=1
out=''
currents=s[0]
for i in range(1,len(s)):
    if s[i]==currents:
        count+=1

    else:
        out=out+str(count)+currents
        count=1
        currents=s[i]
out=out+str(count)+currents
print(out)