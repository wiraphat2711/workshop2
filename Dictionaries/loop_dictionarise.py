thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# EX1
for key in thisdict:
    print(key)

# output:
# brand
# model
# year

# EX2
for key in thisdict:
    print(thisdict[key])

# output
# Ford
# Mustang
# 1964

# EX3
for key in thisdict.keys():
    print(key)

# output
# brand
# model
# year

# EX4
for value in thisdict.values():
    print(value)

# output
# Ford
# Mustang
# 1964

# EX5
for key, value in thisdict.items():
    print(key, value)

# output
# brand Ford
# model Mustang
# year 1964
