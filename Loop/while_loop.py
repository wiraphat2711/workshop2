i = 1
while i < 5:
    print(i)
    i += 1
print(" ")

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print(" ")

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print(" ")

i = 1
while i < 3:
    print(i)
    i += 1
else:
    print("i is no longer less than 3")
print(" ")
