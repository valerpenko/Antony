import random
n=int(input())
random_matrix = [[random.randint(0,10) for j in range(n)] for i in range(n)]
print(random_matrix)
# b=[]
# for i in range(0,len(random_matrix),2):
#     b.append(random_matrix[i])
# b = [item for sublist in b for item in sublist]
# random_matrix=b
# b=[]
# for i in range(1,len(random_matrix),2):
#     b.append(random_matrix[i])
# print(b,sum(b))

s=0
for i in range(0, len(random_matrix),2):
    for j in range(1, len(random_matrix), 2):
        s+=random_matrix[i][j]
print(s)

s=0
for i in range(0, len(random_matrix)):

    for j in range(i%2, len(random_matrix), 2):

        s+=random_matrix[i][j]
print(s)
