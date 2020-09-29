s="import sys; print('Python %s on %s' % (sys.version, sys.platform))"
i=s.find("sys")
print(i)
i+=1
while i>0 :
    i=s.find("sys",i)
    print(i)
    i+=1