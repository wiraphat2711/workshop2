# EXAMPLE1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  # ['apple','cherry']
# EXAMPLE2
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)  # ['apple','cherry']
# EXAMPLE3
thislist = ["apple", "banana", "cherry"]
thislist.pop()  # เอาตัวสุดท้ายของlistออก
print(thislist)  # ['apple','banana']
# EXAMPLE4
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)  # ['banana','cherry']
# EXAMPLE5
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # [ ]
