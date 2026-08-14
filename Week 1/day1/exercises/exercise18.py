# Read a text file and count the number of words.

file = open("sample.txt", "r")

content = file.read()

words = content.split()

print("Number of words:", len(words))

file.close()