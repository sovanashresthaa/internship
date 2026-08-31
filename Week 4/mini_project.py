import os
from google import genai

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

print("AI Text Summarizer")
print("Type 'exit' to quit.")

while True:
    text = input("\nEnter text to summarize: ")

    if text.lower() == "exit":
        print("Goodbye!")
        break

    prompt = f"""
Summarize the following text in 3 concise sentences.

Text:
{text}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    print("\nSummary:")
    print(response.text)

    print("\nThank you for using the AI Text Summarizer!")