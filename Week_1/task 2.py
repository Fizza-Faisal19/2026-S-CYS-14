ecat = float(input("Enter your Ecat marks(out of 400): "))
inter = float(input("Enter your intermediate part 1 marks(out of 1100): "))
matric = float(input("Enter your matric marks(out of 1100): "))
ecat_percent = (ecat / 400) * 100
inter_percent = (inter / 1100) * 100
matric_percent = (matric / 1100) * 100
aggregate = (ecat_percent * 0.33) + (inter_percent * 0.50) + (matric_percent * 0.17)
print("Your Aggregate is:", aggregate, "%")

