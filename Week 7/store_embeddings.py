import json

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct


client = QdrantClient(
    path="./qdrant_db"
)

collection_name = "week7_documents"


with open("documents.txt", "r", encoding="utf-8") as file:
    text = file.read()

chunks = [
    chunk.strip()
    for chunk in text.split("\n\n")
    if chunk.strip()
]


with open("embeddings.json", "r", encoding="utf-8") as file:
    embeddings = json.load(file)


points = []

for i, (chunk, embedding) in enumerate(
    zip(chunks, embeddings)
):
    points.append(
        PointStruct(
            id=i,
            vector=embedding,
            payload={
                "text": chunk
            }
        )
    )


client.upsert(
    collection_name=collection_name,
    points=points
)


print("Embeddings stored successfully!")
print("Documents stored:", len(points))

client.close()