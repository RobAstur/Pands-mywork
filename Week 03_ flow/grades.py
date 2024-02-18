#under_40 = "FAIL"
#Between_40_49 = "PASS"
#Between_50_59 = "MERIT 2"
#Between_60_69 = "MERIT 1"
#Over_70 = distintion

max_grade = 100
lower_grade = 0
grade = ""

while lower_grade >= 0 and max_grade <=100:
    grade = float(input("Write your grade"))
    if grade == -1:
        break
    if grade < lower_grade and grade > max_grade:
        print("Min grade is 0, max grade is 100")
    if grade == 69.5:
        print("distintion")
    elif grade >=0 and grade <40:
        print("FAIL")
    elif grade >= 40 and grade <50:
        print("PASS")
    elif grade >= 50 and grade < 60:
        print("MERIT 2")
    elif grade >= 60 and grade < 70:
        print("Merit 1")
    elif grade >70 and grade <=100:
        print("DISTINTION")
    else:
        print("Max grade is 100, lower grade is 0")



# could have done easier like <40, <50,<60. No need or clarify twice teh same 