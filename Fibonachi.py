f1 = 1
f2 = 1
n = int(input("Номер элемента ряда Фибоначчи: "))
i = 0
while i < n - 2:
    fsum = f1 + f2
    f1 = f2
    f2 = fsum
    i += 1
    print(f1)
print(f2)