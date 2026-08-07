# Print the student with the highest mark.

students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 88,
    "David": 95
}

highest = max(students, key=students.get)

print("Top Student:", highest)
print("Marks:", students[highest])