import os
from google import genai

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

prompt = """Summarize the following text in 3 sentences:

Artificial intelligence is a field of computer science that focuses on
creating systems that can perform tasks that normally require human
intelligence. AI is used in areas such as recommendation systems,
language processing, image recognition, and robotics.
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

print("Response:")
print(response.text)