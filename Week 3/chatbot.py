import os
from google import genai
from google.genai import types

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config=types.GenerateContentConfig(
        temperature=0.5,
        max_output_tokens=500,
        system_instruction="""You are a friendly programming tutor.
Explain programming concepts clearly and simply.
Use examples when helpful.
If the user is confused, explain the concept step by step.

Do not use Markdown formatting.
Do not use asterisks (*).
Do not use bold, italics, bullet points, or headings with Markdown symbols.
Use plain text only.
Keep responses concise unless the user asks for a detailed explanation."""
    )
)

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = chat.send_message(user_input)

    print("Bot:", response.text)