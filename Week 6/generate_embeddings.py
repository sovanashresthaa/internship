import os
import json

from google import genai
from google.genai import types

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

with open("documents.txt", "r", encoding="utf-8") as file:
    text = file.read()

chunks = [
    chunk.strip()
    for chunk in text.split("\n\n")
    if chunk.strip()
]

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=chunks,
    config=types.EmbedContentConfig(
        output_dimensionality=768
    )
)

embeddings = [
    embedding.values
    for embedding in result.embeddings
]

with open("embeddings.json", "w", encoding="utf-8") as file:
    json.dump(embeddings, file)

print("Embeddings generated successfully!")
print("Number of embeddings:", len(embeddings))
print("Embedding dimensions:", len(embeddings[0]))