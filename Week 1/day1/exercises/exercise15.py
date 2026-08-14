# Write a function that accepts a list and returns its average.

def average(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return avg


numbers = [10, 20, 30, 40, 50]

print("Average =", average(numbers))