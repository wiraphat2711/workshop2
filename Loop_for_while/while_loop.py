i = 1
while i < 5:
    print(i)
    i += 1
print(" ")  # 1234

i = 1
while i < 6:
    print(i)
    if i == 3:
        break  # ออก
    i += 1
print(" ")  # 123

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # กลับ while
    print(i)
print(" ")  # 12456

i = 1
while i < 3:
    print(i)
    i += 1
else:
    print("i is no longer less than 3")  # i = 3 เกิด else
print(" ")  # 1 2 i is no longer less than 3
