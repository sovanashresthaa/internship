import json

json_data = """
{
    "name": "Python",
    "type": "Programming Language",
    "difficulty": "Beginner",
    "main_use": "Web development, data analysis, automation, and AI"
}
"""

try:
    data = json.loads(json_data)

    print("Valid JSON!")
    print("Name:", data["name"])
    print("Type:", data["type"])
    print("Difficulty:", data["difficulty"])
    print("Main use:", data["main_use"])

except json.JSONDecodeError:
    print("Invalid JSON!")