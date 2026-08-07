# Count how many even and odd numbers are in a list.

numbers = [10, 15, 22, 33, 48, 51, 64]

even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even:", even_count)
print("Odd:", odd_count)