
def dec2bin():
    pass

def cycleShift():
    pass

def bin2dec():
    pass

n=int(input())

nbin=dec2bin(n)
max=n
curbin = cycleShift(nbin)
while curbin!=nbin:
    if bin2dec(curbin)>max:
        max=bin2dec(curbin)
    curbin = cycleShift(curbin)




