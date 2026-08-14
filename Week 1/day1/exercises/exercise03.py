# Reverse a list without using reverse() or slicing.

numbers = [10, 20, 30, 40, 50]

reversed_list = []

for item in numbers:
    reversed_list = [item] + reversed_list

print(reversed_list)