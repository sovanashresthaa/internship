import os
from google import genai

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

prompt = """
Give information about Python programming using exactly this JSON format:

{
  "name": "",
  "type": "",
  "difficulty": "",
  "main_use": ""
}

Return only valid JSON. Do not include explanations or Markdown.
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

print("Response:")
print(response.text)