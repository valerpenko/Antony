def polynomMember(k,index):
    if k==0:
        return  ""

    if k<0:
        k=-k
        s="-"
    else:
        s="+"

    if index==0:
        return s+str(k)
    elif index==1:
        return s + str(k)+"*x"
    else:
        return s+str(k)+"*x^"+str(index)

koeffs=[0,4,-5,0,7]
s=""
for i in range(len(koeffs)):
    part=polynomMember(koeffs[i],i)
    s=s+part
if s[0]=="+":
    s=s[1:]
print(s)
