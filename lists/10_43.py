def sum1(lst):
    print("вошли в sum1")
    total = 0
    for element in lst:
        if (type(element) == list):
            total = total + sum1(element)
        else:
            total = total + element
    return total
print(sum1([1,[ 2, 3], 4]))