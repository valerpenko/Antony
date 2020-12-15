a=[[4,9,7,6],
   [3,6,4,0],
   [8,9,7,5],
   [5,3,7,6]]
s=0
for r in range(len(a)):
   for c in range(r+1,len(a)):
      s=s+a[r][c]
      print(a[r][c])


print(s)