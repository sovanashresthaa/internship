import os
import numpy as np
from google import genai

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

query = "I want to learn Python programming."

sentences = [
    "Python is a popular programming language.",
    "I enjoy playing football with my friends.",
    "Python can be used for artificial intelligence.",
    "The weather is sunny today.",
    "Programming languages help us build software."
]


def get_embedding(text):
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )
    return result.embeddings[0].values


def cosine_similarity(vector_a, vector_b):
    vector_a = np.array(vector_a)
    vector_b = np.array(vector_b)

    return np.dot(vector_a, vector_b) / (
        np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    )


query_embedding = get_embedding(query)

results = []

for sentence in sentences:
    sentence_embedding = get_embedding(sentence)
    score = cosine_similarity(query_embedding, sentence_embedding)

    results.append((sentence, score))

results.sort(key=lambda x: x[1], reverse=True)

print("Query:", query)
print("\nRanked Results:\n")

for rank, (sentence, score) in enumerate(results, start=1):
    print(f"{rank}. {sentence}")
    print(f"   Similarity: {score:.4f}\n")