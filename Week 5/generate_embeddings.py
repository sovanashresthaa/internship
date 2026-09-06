import os
from google import genai

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

sentences = [
    "I love programming in Python.",
    "Python is my favorite programming language.",
    "I enjoy playing football.",
    "The weather is beautiful today."
]

for sentence in sentences:
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=sentence
    )

    embedding = result.embeddings[0].values

    print("\nSentence:", sentence)
    print("Embedding length:", len(embedding))
    print("First 5 values:", embedding[:5])