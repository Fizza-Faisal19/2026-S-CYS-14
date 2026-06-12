large = lambda a, b: a if a > b else b
def table(num):
    limit = int(input("Enter range: "))
    for i in range(1, limit + 1):
        print(num, "x", i, "=", num * i)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
big = large(num1, num2)
print("Larger number is:", big)
table(big)
