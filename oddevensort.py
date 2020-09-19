seq=[2,3,16,27,4,2,1]
tmp=[]
for i in range(0,len(seq)):
    if seq[i]%2==0:
        tmp.insert(0,seq[i])
    else:
        tmp.append(seq[i])
seq=tmp
print(tmp)
print(seq)
