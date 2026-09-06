import os
import numpy as np
from google import genai

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

sentences = [
    "Python is a popular programming language.",
    "Machine learning allows computers to learn from data.",
    "Artificial intelligence enables computers to perform intelligent tasks.",
    "Football is a popular sport played around the world.",
    "Nepal is known for its beautiful mountains and trekking routes."
]


def get_embedding(text):
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )
    return result.embeddings[0].values


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


# Generate embeddings for all sentences
result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=sentences
)

document_embeddings = [
    embedding.values for embedding in result.embeddings
]

print("Semantic Search")
print("Type 'exit' to quit.")

while True:
    query = input("\nSearch: ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    query_embedding = get_embedding(query)

    results = []

    for sentence, embedding in zip(sentences, document_embeddings):
        score = cosine_similarity(query_embedding, embedding)
        results.append((sentence, score))

    results.sort(key=lambda x: x[1], reverse=True)

    print("\nMost relevant results:")

    for rank, (sentence, score) in enumerate(results[:3], start=1):
        print(f"{rank}. {sentence}")
        print(f"   Similarity: {score:.4f}")