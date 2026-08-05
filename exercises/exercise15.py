#count lines in a file

with open("sample.txt", "r") as file:
    lines = file.readlines()

print("Total lines:", len(lines))