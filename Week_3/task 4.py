def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
c = float(input("Enter Celsius: "))
f = float(input("Enter Fahrenheit: "))
print("Fahrenheit =", celsius_to_fahrenheit(c))
print("Celsius =", fahrenheit_to_celsius(f))
