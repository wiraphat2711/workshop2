# is เชค value,address  == เชคเเต่ value

# ex1
int1 = 5
int2 = 5

string1 = "Hello"
string2 = "Hello"

float1 = 0.1
float2 = 0.1

print(int1 is int2)  # output:True
print(string1 is string2)  # output:True
print(float1 is float2)  # output:True

# ex2
# Tuple,Set,List
dict1 = {"name": "pipusna", "age": "26"}
dict2 = {"name": "pipusna", "age": "26"}
dict3 = dict1

print(dict1 is dict3)  # output:True
print(dict1 is dict2)  # output:False ค่าหมือนกันเเต่ address คนละที่
print(dict1 == dict2)  # output:True ดูเเต่ value
# Tuple,Set,List
