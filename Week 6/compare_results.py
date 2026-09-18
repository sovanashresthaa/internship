import os
import json
import math

from google import genai
from google.genai import types

from qdrant_client import QdrantClient


gemini_client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

query = input("Enter a search query: ")

with open("documents.txt", "r", encoding="utf-8") as file:
    text = file.read()

chunks = [
    chunk.strip()
    for chunk in text.split("\n\n")
    if chunk.strip()
]

with open("embeddings.json", "r", encoding="utf-8") as file:
    embeddings = json.load(file)


def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))

    magnitude_a = math.sqrt(sum(x * x for x in a))
    magnitude_b = math.sqrt(sum(y * y for y in b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0

    return dot_product / (magnitude_a * magnitude_b)


result = gemini_client.models.embed_content(
    model="gemini-embedding-001",
    contents=query,
    config=types.EmbedContentConfig(
        output_dimensionality=768
    )
)

query_embedding = result.embeddings[0].values


manual_results = []

for chunk, embedding in zip(chunks, embeddings):
    score = cosine_similarity(query_embedding, embedding)
    manual_results.append((score, chunk))

manual_results.sort(
    reverse=True,
    key=lambda x: x[0]
)

print("\nWeek 5 Manual Similarity Results:")

for i, (score, chunk) in enumerate(manual_results[:3], start=1):
    print(f"\n{i}. Score: {score:.4f}")
    print(chunk)


db_client = QdrantClient(
    path="./qdrant_db"
)

database_results = db_client.query_points(
    collection_name="internship_documents",
    query=query_embedding,
    limit=3
).points

print("\nWeek 6 Vector Database Results:")

for i, result in enumerate(database_results, start=1):
    print(f"\n{i}. Score: {result.score:.4f}")
    print(result.payload["text"])

db_client.close()