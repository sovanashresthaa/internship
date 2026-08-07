# Create a text file and write five lines of text to it.

file = open("sample.txt", "w")

file.write("This is line 1.\n")
file.write("This is line 2.\n")
file.write("This is line 3.\n")
file.write("This is line 4.\n")
file.write("This is line 5.\n")

file.close()

print("Data written successfully.")