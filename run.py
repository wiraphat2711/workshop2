# number_list = [1, 1, 1, 2, 2, 2, 3, 3, 3]  # [1,2,3]
# EX1
# result = []
# for number in number_list:
#    if not number in result:
#        result.append(number)
# print(result)

# EX2
# print(list(set(number_list)))

# print([number for number in number_list if not number in result])


# pass by reference เพิ่มค่าใส่ตัวเเปลที่เข้าฟังชั้นด้วยใน address เดิม  python
# pass by value ไม่เพิ่มค่าเข้าตัวเเปลที่ผ่านฟังชัน
def add_number(number):
    return number + 1


number = 1
result = add_number(number)
print("result", result)  # 2


def edit_dict(dict):
    dict["nickname"] = "pai"


profile = {"name": "wiraphat", "age": 20}
edit_dict(profile)
print("profile", profile)
