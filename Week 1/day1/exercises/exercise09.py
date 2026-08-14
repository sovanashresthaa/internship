# Print the multiplication table (1–10) for a user-entered number.

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)