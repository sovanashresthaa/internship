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

collection_name = "week7_documents"


questions = [
    "What is machine learning?",
    "What is RAG?",
    "What is Qdrant?",
    "What is Nepal known for?",
    "What is the capital of France?"
]


for question in questions:

    print("\n" + "=" * 60)
    print("Question:", question)

    # Generate query embedding
    result = gemini_client.models.embed_content(
        model="gemini-embedding-001",
        contents=question,
        config=types.EmbedContentConfig(
            output_dimensionality=768
        )
    )

    query_embedding = result.embeddings[0].values


    # Retrieve relevant context
    results = db_client.query_points(
        collection_name=collection_name,
        query=query_embedding,
        limit=3
    ).points


    context = "\n\n".join(
        result.payload["text"]
        for result in results
    )


    prompt = f"""
Answer the question using only the provided context.

If the answer is not supported by the context, say:
"I don't have enough information in the provided context."

Do not invent information.

Context:
{context}

Question:
{question}

Answer:
"""


    response = gemini_client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=200
        )
    )


    print("\nRetrieved Context:")
    print(context)

    print("\nAnswer:")
    print(response.text)


db_client.close()