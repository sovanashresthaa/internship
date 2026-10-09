import os
import logging

# Reduce noisy Gemini SDK logs
logging.getLogger("google.genai").setLevel(logging.ERROR)
logging.getLogger("google_genai").setLevel(logging.ERROR)
logging.getLogger("langchain_google_genai").setLevel(logging.ERROR)

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# --------------------------------------------------
# GEMINI MODEL USING LANGCHAIN
# --------------------------------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.environ.get("GEMINI_API_KEY"),
    temperature=0.5,
    max_output_tokens=500
)


# --------------------------------------------------
# CONVERSATION MEMORY
# --------------------------------------------------

conversation_history = [
    SystemMessage(
        content=(
            "You are a friendly programming tutor. "
            "Explain programming concepts clearly and step by step. "
            "Use simple examples when helpful."
        )
    )
]


# --------------------------------------------------
# CHAT LOOP
# --------------------------------------------------

print("================================")
print("       LangChain Chatbot")
print("================================")
print("Ask me a question.")
print("The chatbot can remember the conversation.")
print("Type 'exit' to quit.\n")


while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    try:
        # Add the user's message to memory
        conversation_history.append(
            HumanMessage(content=user_input)
        )

        # Send the conversation history to Gemini
        response = llm.invoke(conversation_history)

        # Display the response
        if isinstance(response.content, str):
            print("Bot:", response.content)
        else:
            for item in response.content:
                if isinstance(item, dict) and item.get("type") == "text":
                    print("Bot:", item["text"])

        # Add the AI response to memory
        conversation_history.append(
            AIMessage(content=response.content)
        )

    except Exception:
        print("Bot: Sorry, the Gemini service is temporarily unavailable.")
        print("Please try again in a moment.")