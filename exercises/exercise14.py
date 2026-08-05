#append text to a file

with open("sample.txt", "a") as file:
    file.write("\nWelcome to Python!")
print("Text appended successfully.")