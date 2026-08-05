#prime number

number = int(input("Enter a number: "))
if number < 2:
    print("Not Prime")
else:
    prime = True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            prime = False
            break

    if prime:
        print("Prime")
    else:
        print("Not Prime")