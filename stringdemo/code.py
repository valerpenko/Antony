msg=input()
first=msg[0:len(msg):2]
reversedf=first[::-1]
second=msg[1:len(msg):2]
end=reversedf+second
print(end)

if len(end)%2==0:
    first=end[0:len(end)//2]
    rfirst=first[::-1]
    second=end[(len(end)//2):]
    res=''

    print(first)
    print(second)
    for i in range(0,len(first)):
        res+=rfirst[i]+second[i]


else:
    first=end[0:len(end)//2+1]
    rfirst = first[::-1]
    second=end[(len(end)//2)+1:]
    res=''

    print(first)
    print(second)
    for i in range(0,len(second)):
        res+=rfirst[i]+second[i]
    res+=rfirst[-1]
print(res)