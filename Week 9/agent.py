import os
from google import genai
from google.genai import types


# --------------------------------------------------
# TOOL: Calculator
# --------------------------------------------------

def calculate(expression: str) -> str:
    """Calculate a mathematical expression."""

    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)

    except Exception:
        return "Sorry, I could not calculate that expression."


# --------------------------------------------------
# GEMINI CLIENT
# --------------------------------------------------

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)


# --------------------------------------------------
# AI AGENT
# --------------------------------------------------

chat = client.chats.create(
    model="gemini-3.8-flash",
    config=types.GenerateContentConfig(
        system_instruction=(
            "You are a helpful AI assistant. "
            "Use the calculator tool whenever the user asks "
            "you to perform a mathematical calculation."
        ),
        tools=[calculate]
    )
)


# --------------------------------------------------
# CHAT LOOP
# --------------------------------------------------

print("================================")
print("       AI Calculator Agent")
print("================================")
print("Ask me a question.")
print("Type 'exit' to quit.\n")


while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    try:
        response = chat.send_message(user_input)
        print("Bot:", response.text)

    except Exception as e:
        print("Bot: Sorry, the Gemini service is temporarily unavailable.")
        print("Please try again in a moment.")