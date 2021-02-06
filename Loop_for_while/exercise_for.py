number1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
number2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for i in number1:
    print("    [", i, "]")
    for j in number2:
        print(i, " * ", j, " : ", i * j)
    print("----------------")
