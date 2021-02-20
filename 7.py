string_upper_list = []
string_list = ["jim", "por", "bb"]
for string in string_list:
    string_upper_list.append(string.upper())
print(string_upper_list)
print(string_list)

# string_list = ["jim", "por", "bb"]
# string_upper_list = [string.upper() for string in string_list]
# print(string_upper_list)

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [number for number in number_list if number > 5]
print(result)