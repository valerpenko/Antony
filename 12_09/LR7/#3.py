str="101010111001"
str1=""
for i in range(0,len(str)):
    if str[i]=="0":
        str1=str1+"1"
    else:
        str1 = str1 + "0"
print(str1)