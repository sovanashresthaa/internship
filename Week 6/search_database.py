import os

from google import genai
from google.genai import types
from qdrant_client import QdrantClient


gemini_client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

db_client = QdrantClient(
    path="./qdrant_db"
)

collection_name = "internship_documents"

query = input("Search: ")

result = gemini_client.models.embed_content(
    model="gemini-embedding-001",
    contents=query,
    config=types.EmbedContentConfig(
        output_dimensionality=768
    )
)

query_embedding = result.embeddings[0].values

results = db_client.query_points(
    collection_name=collection_name,
    query=query_embedding,
    limit=3
).points

print("\nMost relevant results:")

for i, result in enumerate(results, start=1):
    print(f"\n{i}. Score: {result.score:.4f}")
    print(result.payload["text"])

db_client.close()