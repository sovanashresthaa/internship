# Week 6 - Vector Databases

## Objective

The objective of Week 6 was to understand vector databases and use a lightweight local vector database for semantic search.

## Tasks Completed

1. Set up a local Qdrant vector database.
2. Loaded a small collection of documents.
3. Split the documents into chunks.
4. Generated embeddings using Gemini.
5. Stored the embeddings in the vector database.
6. Queried the database using semantic similarity.
7. Compared the vector database approach with the manual similarity approach from Week 5.

## Technologies Used

- Python
- Gemini API
- Gemini Embedding Model
- Qdrant
- JSON

## Vector Database

Qdrant was used as a local vector database.

The database stores document embeddings and allows relevant documents to be retrieved using vector similarity.

## Embeddings

The Gemini `gemini-embedding-001` model was used to convert documents and queries into numerical vectors.

The embeddings were generated with a dimensionality of 768.

## Semantic Search

A user's query is converted into an embedding and compared with the document vectors stored in Qdrant.

The most relevant document chunks are then returned.

## Week 5 vs Week 6

In Week 5, similarity was calculated manually using cosine similarity.

In Week 6, embeddings were stored in a vector database and the database was queried directly for the most relevant results.

## Result

A working semantic search system was created using a local vector database.