# Week 8 Internship Documentation

## Building a Simple RAG Application

### Objective

The objective of Week 8 was to convert the RAG workflow developed in Week 7 into a simple usable application. The application allows users to upload documents and ask questions about their content.

## Application Workflow

The application follows these steps:

1. User uploads text documents.
2. The documents are split into smaller chunks.
3. Gemini generates embeddings for the chunks.
4. The embeddings are stored in a Qdrant vector database.
5. The user enters a question.
6. The question is converted into an embedding.
7. Qdrant retrieves the most relevant document chunks.
8. The retrieved context is sent to Gemini.
9. Gemini generates an answer based on the retrieved context.

## Technologies Used

- Python
- Streamlit
- Gemini API
- Gemini Embedding API
- Qdrant
- Vector embeddings
- Semantic search
- Retrieval Augmented Generation

## Features

- Upload multiple text documents
- Process uploaded documents
- Generate document embeddings
- Store embeddings in Qdrant
- Ask questions about uploaded documents
- Retrieve relevant context
- Generate context-based answers
- Display retrieved context and similarity scores
- Handle missing documents
- Handle empty questions
- Handle processing errors

## Error Handling

The application checks whether documents have been uploaded before processing questions. It also checks for empty questions and displays an error message when document processing or question answering fails.

If the requested information is not available in the provided documents, the RAG prompt instructs the language model to state that sufficient information is not available rather than inventing an answer.

## Testing

The application was tested with questions related to:

- Machine learning
- Retrieval Augmented Generation
- Qdrant
- Nepal

An additional question about the capital of France was tested even though the information was not included in the document collection. This was used to test how the application handles information that is unavailable in the provided documents.

