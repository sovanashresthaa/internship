# Write a function that takes two numbers and returns their GCD.

def gcd(a, b):

    while b != 0:
        a, b = b, a % b

    return a


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("GCD =", gcd(num1, num2))