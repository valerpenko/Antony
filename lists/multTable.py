table=[]
for i in range(1,10):
    table.append([i,5,i*5])
for i in range(9):
    print(table[i])

table=[ [i,5,i*5] for i in range(1,10)]
for i in range(9):
    print(table[i])
