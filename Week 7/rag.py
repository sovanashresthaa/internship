import os

from google import genai
from google.genai import types

from qdrant_client import QdrantClient


# --------------------------------------------------
# Gemini client
# --------------------------------------------------

gemini_client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)


# --------------------------------------------------
# Qdrant client
# --------------------------------------------------

db_client = QdrantClient(
    path="./qdrant_db"
)

collection_name = "week7_documents"


# --------------------------------------------------
# RAG function
# --------------------------------------------------

def answer_question(question):

    # Generate embedding for the question
    embedding_result = gemini_client.models.embed_content(
        model="gemini-embedding-001",
        contents=question,
        config=types.EmbedContentConfig(
            output_dimensionality=768
        )
    )

    query_embedding = embedding_result.embeddings[0].values


    # Retrieve relevant documents
    search_results = db_client.query_points(
        collection_name=collection_name,
        query=query_embedding,
        limit=3
    ).points


    # Build context
    context_parts = []

    for result in search_results:
        context_parts.append(
            result.payload["text"]
        )

    context = "\n\n".join(context_parts)


    # Create grounded prompt
    prompt = f"""
You are a helpful question-answering assistant.

Answer the user's question using only the information provided
in the context below.

If the answer cannot be found in the context, clearly say:
"I don't have enough information in the provided context."

Do not invent facts or add information that is not supported
by the context.

Context:
{context}

Question:
{question}

Answer:
"""


    # Generate answer
    response = gemini_client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=300
        )
    )

    return context, response.text


# --------------------------------------------------
# Main program
# --------------------------------------------------

print("RAG Question Answering System")
print("Type 'exit' to quit.")

while True:

    question = input("\nQuestion: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    context, answer = answer_question(question)

    print("\nRetrieved Context:")
    print(context)

    print("\nGenerated Answer:")
    print(answer)


db_client.close()