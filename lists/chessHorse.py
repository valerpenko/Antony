# i,j - позиция коня на пустой шаматной доске.
# Сколько есть ходов у коня?
row=0
col=0
row=row+1
col=col+1
board=[ [1 for j in range(-2,10)] for i in range(-2,10)]
print(board)
for i in range(2,10):
    for j in range(2, 10):
        board[i][j]=0
print(board)
movecount=0
offset=[[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]
for i in range(0,8):
    if board[row-offset[i][0]][col-offset[i][1]]==0:
        movecount+=1
print(movecount)
