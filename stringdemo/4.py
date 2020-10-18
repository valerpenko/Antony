s = input()
# s=s[::-1]
# print(s)
x=''
for i in range(0,len(s)):
    x=s[0]+x
    print(x)
    s=s[1:len(s)]
    print(s)

