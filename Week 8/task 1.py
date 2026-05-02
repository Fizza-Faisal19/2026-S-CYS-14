student_dict = {}

ob_marks = int(input("Enter total marks: "))
total_marks = int(input("Enter total marks: "))
if total_marks <= 0 or total_marks > 300:
    print("Enter valid numbers")
elif ob_marks > total_marks:
    print("enter valid numbers")
else:
    result = (ob_marks / total_marks) * 100
    print(result)
    if result >= 90:
        print("A+")
    elif result >= 85:
        print("A-")
    elif result >= 80:
        print("B+")
    elif result >= 75:
        print("B-")
    elif result >= 70:
        print("C+")
    elif result >= 65:
        print("C-")
    elif result >= 60:
        print("F")
total_students = int(input("Enter number of students: "))
for i in range(total_students+1):
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    student_list = [(name, marks)]
    for key, value in student_list:
        student_dict.setdefault (key, []).append(value)

print(student_dict)