def average(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    avg = sum / len(numbers)
    print("Average =", avg)
average(15, 20, 11, 9)

