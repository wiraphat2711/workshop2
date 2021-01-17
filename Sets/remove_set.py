# EX1
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)  # {'apple','cherry'}

# EX2
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)  # {'cherry','apple'}

# EX3
thisset = {"apple", "banana", "cherry"}
thisset.pop()  # สุ่มเอาค่าค่า1ออกไป
print(thisset)  # {'cherry','banana'}

# EX4
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)  # set( )
