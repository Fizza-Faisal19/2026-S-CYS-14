for i in range(1, 4):
    for j in range(2, 4):
        print(f"{i} and {j}")

for i in range(1, 10):
    for j in range(1, i+1):
        print("*", end="")



stars = 10
for i in range(stars):
    spaces = stars - i - 1
    print(' ' * spaces + "*" * (2*i +1))