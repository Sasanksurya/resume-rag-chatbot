
import streamlit as st

from pdf_loader import extract_text_from_pdf
from chunking import create_chunks
from embeddings import get_embeddings
from vector_store import create_vector_store
from rag_chain import get_answer

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="Resume RAG Chatbot",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume RAG Chatbot")
st.markdown("Upload a resume and ask questions about it.")

# -------------------------------------------------
# Session State
# -------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "resume_processed" not in st.session_state:
    st.session_state.resume_processed = False

# -------------------------------------------------
# Upload Resume
# -------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

# -------------------------------------------------
# Process Resume
# -------------------------------------------------

if uploaded_file is not None and not st.session_state.resume_processed:

    with st.spinner("Processing Resume..."):

        try:

            # Save uploaded file temporarily
            with open("temp_resume.pdf", "wb") as f:
                f.write(uploaded_file.read())

            # Extract text
            text = extract_text_from_pdf("temp_resume.pdf")

            if not text.strip():
                st.error("Could not extract text from PDF.")
                st.stop()

            # Create chunks
            chunks = create_chunks(text)

            # Create embeddings
            embeddings = get_embeddings()

            # Create FAISS vector store
            create_vector_store(chunks, embeddings)

            st.session_state.resume_processed = True

            st.success("✅ Resume Indexed Successfully!")

        except Exception as e:
            st.error(f"Error while processing PDF: {e}")

# -------------------------------------------------
# Ask Questions
# -------------------------------------------------

if st.session_state.resume_processed:

    st.subheader("Ask Questions")

    question = st.text_input(
        "Enter your question"
    )

    if st.button("Submit Question"):

        if not question.strip():
            st.warning("Please enter a question.")

        else:

            try:

                embeddings = get_embeddings()

                answer, docs = get_answer(
                    question,
                    embeddings
                )

                # Save chat history
                st.session_state.messages.append(
                    {
                        "question": question,
                        "answer": answer
                    }
                )

                # Display answer
                st.subheader("🤖 Answer")
                st.write(answer)

                # Display retrieved chunks
                with st.expander("📄 Retrieved Context"):

                    for i, doc in enumerate(docs):

                        st.markdown(
                            f"### Chunk {i+1}"
                        )

                        st.write(
                            doc.page_content
                        )

            except Exception as e:
                st.error(f"Error while generating answer: {e}")

# -------------------------------------------------
# Chat History
# -------------------------------------------------

if st.session_state.messages:

    st.subheader("💬 Chat History")

    for chat in reversed(
        st.session_state.messages
    ):

        st.markdown(
            f"**🧑 Question:** {chat['question']}"
        )

        st.markdown(
            f"**🤖 Answer:** {chat['answer']}"
        )

        st.divider()
