from rag_engine import (
    create_collection,
    split_documents,
    generate_embeddings,
    store_documents,
    search_documents,
    generate_answer
)


# --------------------------------------------------
# Load sample document
# --------------------------------------------------

with open(
    "documents.txt",
    "r",
    encoding="utf-8"
) as file:

    text = file.read()


# --------------------------------------------------
# Prepare documents
# --------------------------------------------------

chunks = split_documents(text)

print("Number of chunks:", len(chunks))


# --------------------------------------------------
# Create database
# --------------------------------------------------

create_collection()


# --------------------------------------------------
# Generate embeddings
# --------------------------------------------------

embeddings = generate_embeddings(
    chunks
)


# --------------------------------------------------
# Store documents
# --------------------------------------------------

store_documents(
    chunks,
    embeddings
)


print("Documents stored successfully!")


# --------------------------------------------------
# Test questions
# --------------------------------------------------

questions = [
    "What is machine learning?",
    "What is RAG?",
    "What is Qdrant?",
    "What is Nepal known for?",
    "What is the capital of France?"
]


# --------------------------------------------------
# Test RAG
# --------------------------------------------------

for question in questions:

    print("\n" + "=" * 60)

    print("Question:", question)

    results = search_documents(
        question
    )

    answer = generate_answer(
        question,
        results
    )

    print("\nAnswer:")
    print(answer)


print("\nTesting completed successfully!")