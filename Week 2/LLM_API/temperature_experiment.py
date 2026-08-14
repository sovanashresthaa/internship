import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set.")

client = genai.Client(api_key=api_key)

prompt = """
Write a short creative story about a student learning artificial intelligence.
"""

# Lower temperature
response_low = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt,
    generation_config={
        "temperature": 0.2
    }
)

# Higher temperature
response_high = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt,
    generation_config={
        "temperature": 1.0
    }
)

print("\n--- LOW TEMPERATURE (0.2) ---")
print(response_low.output_text)

print("\n--- HIGH TEMPERATURE (1.0) ---")
print(response_high.output_text)

print("\n--- OBSERVATION ---")
print("Lower temperature generally produces more predictable output.")
print("Higher temperature generally allows more variation and creativity.")