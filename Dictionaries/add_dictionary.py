# EX1
thisdict = {"brabd": "ford", "model": "Mustang", "year": 1964}
thisdict["color"] = "red"  # เพิ่ม key
print(thisdict)
# output:{'brabd': 'ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# EX2
thisdict = {"brabd": "ford", "model": "Mustang", "year": 1964}
thisdict.update({"color": "red"})
print(thisdict)
# output:{'brabd': 'ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
