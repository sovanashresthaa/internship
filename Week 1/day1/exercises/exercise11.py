# Find all prime numbers between 1 and 100.

for number in range(2, 101):

    is_prime = True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number)