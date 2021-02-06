# EX1
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print(thisdict)
# output:{'brand': 'Ford', 'year': 1964}

# EX2
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.popitem()  # ลบตัวสุดท้าย
print(thisdict)
# output:{'brand': 'Ford', 'model': 'Mustang'}

# EX3
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict["model"]
print(thisdict)
# output:{'brand': 'Ford', 'year': 1964}

# EX4
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)
# output:{}
