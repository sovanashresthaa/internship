import os

from google import genai
from google.genai import types

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct


# --------------------------------------------------
# Gemini client
# --------------------------------------------------

gemini_client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)


# --------------------------------------------------
# Qdrant settings
# --------------------------------------------------

DB_PATH = "./qdrant_db"
COLLECTION_NAME = "week8_documents"

db_client = None


# --------------------------------------------------
# Get Qdrant client
# --------------------------------------------------

def get_db_client():

    global db_client

    if db_client is None:
        db_client = QdrantClient(
            path=DB_PATH
        )

    return db_client


# --------------------------------------------------
# Close Qdrant
# --------------------------------------------------

def close_database():

    global db_client

    if db_client is not None:

        try:
            db_client.close()
        except Exception:
            pass

        db_client = None


# --------------------------------------------------
# Create collection
# --------------------------------------------------

def create_collection():

    client = get_db_client()

    if client.collection_exists(COLLECTION_NAME):
        client.delete_collection(COLLECTION_NAME)

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=768,
            distance=Distance.COSINE
        )
    )


# --------------------------------------------------
# Split documents
# --------------------------------------------------

def split_documents(text):

    chunks = [
        chunk.strip()
        for chunk in text.split("\n\n")
        if chunk.strip()
    ]

    return chunks


# --------------------------------------------------
# Generate embeddings
# --------------------------------------------------

def generate_embeddings(chunks):

    result = gemini_client.models.embed_content(
        model="gemini-embedding-001",
        contents=chunks,
        config=types.EmbedContentConfig(
            output_dimensionality=768
        )
    )

    return [
        embedding.values
        for embedding in result.embeddings
    ]


# --------------------------------------------------
# Store documents
# --------------------------------------------------

def store_documents(chunks, embeddings):

    client = get_db_client()

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
        collection_name=COLLECTION_NAME,
        points=points
    )


# --------------------------------------------------
# Search documents
# --------------------------------------------------

def search_documents(question, limit=3):

    client = get_db_client()

    result = gemini_client.models.embed_content(
        model="gemini-embedding-001",
        contents=question,
        config=types.EmbedContentConfig(
            output_dimensionality=768
        )
    )

    query_embedding = result.embeddings[0].values

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding,
        limit=limit
    ).points

    return results


# --------------------------------------------------
# Generate answer
# --------------------------------------------------

def generate_answer(question, results):

    if not results:
        return (
            "I could not find relevant information "
            "in the provided documents."
        )

    context = "\n\n".join(
        result.payload["text"]
        for result in results
    )

    prompt = f"""
You are a helpful question-answering assistant.

Answer the user's question using only the information
provided in the context.

Do not invent facts.

If the answer is not available in the context, say:

"I don't have enough information in the provided documents."

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
            max_output_tokens=300
        )
    )

    return response.text