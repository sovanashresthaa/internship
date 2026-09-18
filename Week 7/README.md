# Week 7 Internship Documentation

## Retrieval Augmented Generation Basics

### Objective

The objective of Week 7 was to understand the Retrieval Augmented Generation (RAG) pattern and combine vector database retrieval with a language model to generate answers using retrieved context.

## RAG Workflow

The RAG system follows these steps:

1. The user enters a question.
2. The question is converted into an embedding.
3. The vector database searches for relevant document chunks.
4. The retrieved chunks are provided to the language model as context.
5. The language model generates an answer using the retrieved context.

## Technologies Used

- Python
- Gemini API
- Gemini Embedding API
- Gemini Embedding Model
- Qdrant
- Vector embeddings
- Semantic search

## Vector Database

Qdrant was used as the local vector database. The document embeddings generated using the Gemini embedding model were stored in Qdrant.

## Retrieval

When a user asks a question, the question is converted into a vector using the Gemini embedding model. Qdrant then retrieves the most relevant document chunks based on vector similarity.

## Generation

The retrieved document chunks are added to a prompt and sent to the Gemini language model. The model generates an answer using the retrieved context.

The prompt instructs the model not to invent information and to state when the provided context does not contain enough information.

## Testing

The RAG system was tested using questions about:

- Machine learning
- Artificial intelligence
- RAG
- Qdrant
- Nepal

An additional question outside the provided documents was also tested to observe whether the model would avoid generating unsupported information.

## Result

A working RAG question-answering system was created by combining the Week 6 vector database retrieval process with a Gemini language model.

## Conclusion

The Week 7 work demonstrated how Retrieval Augmented Generation combines information retrieval and language generation. Relevant document chunks were retrieved from a vector database and provided to the language model as context. This allowed the system to generate answers based on the available documents while reducing unsupported responses.