i = 2
while i <= 12:
    num = 1
    print("    [", i, "]")
    while num <= 12:
        print(i, " * ", num, ": ", i * num)
        num += 1
    print("-------------")
    i += 1