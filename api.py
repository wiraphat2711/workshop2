
req -> res 
ร้านอาหารตามสั่ง

พี่อยากกินกระเพราไข่ดาว ไปสั่งร้านอาหารหอเย็น -> req (website)
ไปสั่งร้านอาหารหอเย็น ได้เลยเดียวเรากำลังทำอยู่นะ -> response (server api)
โอเคฉันรอ -> req (website)

#mysql                                           # mongobd

# table account                                  # {"student_id": 5630252488,"student_name": "pipunsa","3/02":[{}]}
# id | name
# 5630252488 | pipusana

# table รายชื่อนิสิตที่ลงทะเบียนเรียน
# student_id | sec_id
# 5630252488 | 10112358

# table รายวิชา
# sec_id | name
# 10112358 | python basic

# mongobd
#{
#    "student_id": 5630252488,
#    "student_name": "pipunsa",
#    "3/02":[
#        {
#            "sec_id": "10112358",
#            "sec_name": "python basic",
#        },
#        {
#            "sec_id": "10112357",
#            "sec_name": "python basic",
#        }
#    ]   
#}