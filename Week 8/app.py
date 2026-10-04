import streamlit as st

from rag_engine import (
    create_collection,
    split_documents,
    generate_embeddings,
    store_documents,
    search_documents,
    generate_answer
)


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Simple RAG Application",
    page_icon="📚",
    layout="centered"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("📚 Simple RAG Application")

st.write(
    "Upload documents and ask questions about their content."
)


# --------------------------------------------------
# Session state
# --------------------------------------------------

if "documents_loaded" not in st.session_state:
    st.session_state.documents_loaded = False


# --------------------------------------------------
# File upload
# --------------------------------------------------

st.header("1. Upload Documents")

uploaded_files = st.file_uploader(
    "Upload one or more text documents",
    type=["txt"],
    accept_multiple_files=True
)


# --------------------------------------------------
# Process documents
# --------------------------------------------------

if st.button("Process Documents"):

    if not uploaded_files:

        st.error(
            "Please upload at least one document."
        )

    else:

        try:

            all_chunks = []

            for uploaded_file in uploaded_files:

                content = uploaded_file.read().decode(
                    "utf-8"
                )

                chunks = split_documents(content)

                all_chunks.extend(chunks)


            if not all_chunks:

                st.error(
                    "The uploaded documents do not contain usable text."
                )

            else:

                with st.spinner(
                    "Generating embeddings and storing documents..."
                ):

                    create_collection()

                    embeddings = generate_embeddings(
                        all_chunks
                    )

                    store_documents(
                        all_chunks,
                        embeddings
                    )

                st.session_state.documents_loaded = True

                st.success(
                    f"Successfully processed {len(all_chunks)} document chunks!"
                )

        except Exception as error:

            st.error(
                f"An error occurred: {error}"
            )


# --------------------------------------------------
# Question section
# --------------------------------------------------

st.header("2. Ask a Question")

question = st.text_input(
    "Enter your question:"
)


# --------------------------------------------------
# Ask button
# --------------------------------------------------

if st.button("Ask"):

    if not st.session_state.documents_loaded:

        st.warning(
            "Please upload and process documents first."
        )

    elif not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        try:

            with st.spinner(
                "Searching documents and generating answer..."
            ):

                results = search_documents(
                    question
                )

                answer = generate_answer(
                    question,
                    results
                )

            st.subheader("Answer")

            st.write(answer)


            # --------------------------------------
            # Retrieved context
            # --------------------------------------

            with st.expander(
                "View Retrieved Context"
            ):

                if results:

                    for i, result in enumerate(
                        results,
                        start=1
                    ):

                        st.write(
                            f"**Result {i}** "
                            f"(Score: {result.score:.4f})"
                        )

                        st.write(
                            result.payload["text"]
                        )

                        st.divider()

                else:

                    st.write(
                        "No relevant context was found."
                    )

        except Exception as error:

            st.error(
                f"Unable to process your question: {error}"
            )