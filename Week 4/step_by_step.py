import os
from google import genai

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

prompt = """
Solve the following problem step by step.

A student has 5 notebooks. Each notebook costs 80 rupees.
How much does the student pay in total?

Explain each step clearly and then provide the final answer.
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

print("Response:")
print(response.text)