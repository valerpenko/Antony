def sum1(lst):
    total = 0
    for element in lst:
        if (type(element) == (int)):
            total = total + 1
    return total
print(sum1([1, 2, [3,'d'],'12',5, 4]))