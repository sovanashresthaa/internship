# Invert a dictionary (swap keys and values).

student = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 95
}

inverted = {}

for key, value in student.items():
    inverted[value] = key

print(inverted)