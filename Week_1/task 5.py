import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = (b * b) - (4 * a * c)
if d == 0:
    print("Roots are real and equal")
elif d > 0:
    print("Roots are real and distinct")
else:
    print("Roots are imaginary")
if d >= 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Root 1 =", root1)
    print("Root 2 =", root2)