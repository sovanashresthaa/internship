# Write a function that returns the factorial of a number.

def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result


num = int(input("Enter a number: "))

print("Factorial =", factorial(num))