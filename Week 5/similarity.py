import os
import numpy as np
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

embeddings = []

for sentence in sentences:
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=sentence
    )

    embeddings.append(result.embeddings[0].values)


def cosine_similarity(vector_a, vector_b):
    vector_a = np.array(vector_a)
    vector_b = np.array(vector_b)

    return np.dot(vector_a, vector_b) / (
        np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    )


print("Cosine Similarity Results:\n")

for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):
        score = cosine_similarity(embeddings[i], embeddings[j])

        print(f"Sentence {i + 1} vs Sentence {j + 1}: {score:.4f}")