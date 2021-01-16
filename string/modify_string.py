string = " Hello, World! "

print(string.upper())  # " HELLO, WORLD! "
print(string.lower())  # " hello, world! "
print(string.strip())  # "Hello, World!" ตัดสเปกบาหัวท้ายทิ้ง
print(string.replace("H", "J"))  # Jello, World! เเก้ไขคำ
print(string.split(","))  # [' Hello', ' World! '] ตัดคำ รีซอลที่ได้เป็นlist
print(len(string))  # 15 นับอักขระ

input_email = " wiraphat.a@ku.th  "
email = input_email.strip()
# "wiraphat.a@ku.th"
