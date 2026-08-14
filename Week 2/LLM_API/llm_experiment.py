import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set.")

client = genai.Client(api_key=api_key)

# Experiment 1: Basic prompt
prompt1 = "Explain artificial intelligence in simple words."

response1 = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt1
)

print("\n--- Experiment 1: Basic Prompt ---")
print(response1.output_text)


# Experiment 2: More specific prompt
prompt2 = """
Explain artificial intelligence to a beginner.
Use simple language and give one real-world example.
"""

response2 = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt2
)

print("\n--- Experiment 2: Specific Prompt ---")
print(response2.output_text)