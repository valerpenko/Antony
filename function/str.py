def mysplit(str,seps):
    for i in range(0,len(seps)):
        str=str.replace(seps[i]," ")
        print(str)
    res=[]
    w=''
    for i in range(0,len(str)):
        if str[i]!=' ':
            w+=str
        else:
            res.append(w)

    return res


a='Hello! How are you?'

s=[" ",",",":","?","!" ]
print(mysplit(a,s))