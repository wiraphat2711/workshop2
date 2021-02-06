thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# EX1 เอา key ใน thisdict
for key in thisdict:
    print(key)

# output:
# brand
# model
# year
print("  ")
# EX2 เอา value ใน thisdict
for key in thisdict:
    print(thisdict[key])

# output
# Ford
# Mustang
# 1964
print("  ")
# EX3 .key
for key in thisdict.keys():
    print(key)

# output
# brand
# model
# year
print("  ")
# EX4 .value
for value in thisdict.values():
    print(value)

# output
# Ford
# Mustang
# 1964
print("  ")
# EX5 .item
for key, value in thisdict.items():
    print(key, value)

# output
# brand Ford
# model Mustang
# year 1964
