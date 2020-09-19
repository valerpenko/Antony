
for i in range(5):
  if i==0 or i==4:
    for j in range(6):
      print('*',end='')
    print()
  else:
    print('*',end='')
    for j in range(1,5):
      print(' ',end='')
    print('*',end='')
    print()