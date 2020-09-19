km=int(input())
days=int(input())

while km<days:
    km*= 1.1
    days+=1
print(km,days)