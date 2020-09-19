w = 4 #int(input('Ширина: '))
h = 4 #int(input('Высота: '))
r = 3 #int(input('Строк: '))
c = 4 #int(input('Столбцов : '))
for i in range(h*r-r+1):
    if i % (h-1)==0:
        for j in range(w*c-c+1):
           print('*',end='')
        print()
    else:
        for j in range(w * c - c + 1):
            if j % (w - 1) == 0:
                print('*',end='')
            else:
                print(' ',end='')
        print()

# for i in range(h):
#   if i==0 or i==h-1:
#     for j in range(w):
#       print('*',end='')
#     print()
#   else:
#     print('*',end='')
#     for j in range(1,w-1):
#       print(' ',end='')
#     print('*',end='')
#     print()