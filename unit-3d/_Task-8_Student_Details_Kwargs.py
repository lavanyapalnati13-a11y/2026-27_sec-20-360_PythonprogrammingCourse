def student_details(**details):
    for key, value in details.items():
        print(key, ":", value)

student_details(name="Krishna", Maths=90, Physics=85, Chemistry=88)
