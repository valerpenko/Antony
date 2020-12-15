def fb(a):
    if a==1:
        return 1
    if a==2:
        return 2
        return fb(a-2)+fb(a-1)


a=int(input())
print(fb(a))