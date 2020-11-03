str="1010101100"
s=str.replace("0","")
if len(s)%2==0:
    str=str+"0"
else:
    str = str + "1"
print(str)

