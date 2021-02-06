string = "Hello world"
print("H" in string)
# output:True
print("hELLo" not in string)
# output:True

dictObject = {"name": "Jim & Por", "age": "26"}
print("name" in dictObject)
# output:True
print("Jim & Por" in dictObject)
# output:False

number_list = [1, 2, 3]
print(1 in number_list)
# output:True
print(5 in number_list)
# output:False

name_list = ["jim", "por"]
print("jim" in name_list)
# output:True
print("korn" in name_list)
# output:False
