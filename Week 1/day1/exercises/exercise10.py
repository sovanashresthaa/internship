# Print the first 20 Fibonacci numbers using a loop.

first = 0
second = 1

for i in range(20):
    print(first)
    next_number = first + second
    first = second
    second = next_number