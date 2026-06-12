def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact
def permutation(n, r):
    return factorial(n) // factorial(n - r)
def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))
n = int(input("Enter n: "))
r = int(input("Enter r: "))
print("Permutation =", permutation(n, r))
print("Combination =", combination(n, r))
