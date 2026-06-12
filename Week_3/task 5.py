def calculate_gpa():
    subjects = int(input("Enter number of subjects: "))
    total_points = 0
    total_credit_hours = 0
    for i in range(subjects):
        gp = float(input("Enter grade point: "))
        ch = int(input("Enter credit hours: "))
        total_points = total_points + (gp * ch)
        total_credit_hours = total_credit_hours + ch
    gpa = total_points / total_credit_hours
    return gpa
print("GPA =", calculate_gpa())
