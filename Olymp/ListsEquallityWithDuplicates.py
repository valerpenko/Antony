a=[1,4,4,3]
b=[3,4,1]

for elA  in a:
    for iB in range(len(b)):
        if elA==b[iB]:
            del b[iB]
            break
        else:
            if iB==len(b)-1:
                print("No")
                exit()
print("yes")

