import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set.")

client = genai.Client(api_key=api_key)

# Prompt 1
prompt1 = "Explain artificial intelligence."

response1 = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt1
)

print("\n===== PROMPT 1 =====")
print(prompt1)
print("\n===== RESPONSE 1 =====")
print(response1.output_text)


# Prompt 2
prompt2 = """
You are an AI teacher.
Explain artificial intelligence to a beginner.
Use very simple language and give one real-world example.
"""

response2 = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt2
)

print("\n===== PROMPT 2 =====")
print(prompt2)
print("\n===== RESPONSE 2 =====")
print(response2.output_text)