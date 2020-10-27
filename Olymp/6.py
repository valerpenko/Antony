s=input()
n=input()
if s.isalpha()==True and n.isalnum()==True:
    if len(s)>len(n):
        print(s.upper())
    else:
        print(s)
