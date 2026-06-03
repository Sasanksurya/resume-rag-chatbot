
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

st.markdown("""
<h1 style='text-align:center;color:white;'>
🚀 Resume Intelligence Assistant
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style='text-align:center;color:#cbd5e1;'>
AI-Powered Resume Analysis using RAG, FAISS and Groq
</h3>
""", unsafe_allow_html=True)

# ---------------------------------
# Project Metrics
# ---------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("LLM", "Groq")

with col2:
    st.metric("Vector DB", "FAISS")

with col3:
    st.metric("Framework", "LangChain")
# -------------------------------------------------
# Session State
# -------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "resume_processed" not in st.session_state:
    st.session_state.resume_processed = False


# -------------------------------------------------
# Sidebar
# -------------------------------------------------

with st.sidebar:

    st.title("🚀 Resume AI")

    st.success("Resume RAG Chatbot")

    st.markdown("---")

    st.write("### Tech Stack")

    st.write("🤖 Groq LLM")
    st.write("🧠 LangChain")
    st.write("📊 FAISS")
    st.write("📄 PyPDF")
    st.write("⚡ Streamlit")

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -------------------------------------------------
# Upload Resume
# -------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)


# -------------------------------------------------
# ATS Resume Analyzer
# -------------------------------------------------

st.subheader("🎯 ATS Resume Analyzer")

job_description = st.text_area(
    "Paste Job Description Here",
    height=200,
    key="job_description"
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
            st.session_state["resume_text"] = text

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

# =================================================
#  ATS CODE HERE
# =================================================

if st.session_state.resume_processed:

    if job_description.strip():

        if st.button("🎯 Check ATS Score", key="ats_button"):

            resume_text = st.session_state["resume_text"]

            resume_words = set(
                resume_text.lower().split()
            )

            jd_words = set(
                job_description.lower().split()
            )

            matched_words = (
                resume_words.intersection(jd_words)
            )

            score = (
                len(matched_words)
                /
                max(len(jd_words), 1)
            ) * 100

            st.subheader("📊 ATS Analysis Dashboard")

            st.metric(
                "ATS Score",
                f"{score:.1f}%"
            )

            st.progress(min(int(score), 100))


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

    for chat in reversed(st.session_state.messages):

        with st.chat_message("user"):
            st.write(chat["question"])

        with st.chat_message("assistant"):
            st.write(chat["answer"])


# -------------------------------------------------
# Footer
# -------------------------------------------------

st.markdown("---")

st.markdown(
    """
    <center>
    🚀 Built with Streamlit • LangChain • FAISS • Groq
    </center>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# Custom CSS
# -------------------------------------------------

st.markdown("""
<style>
...
your css here
...
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Banner Image
# -------------------------------------------------

st.image(
    "assets/ai_banner.png",
    use_container_width=True
)

st.set_page_config(
    page_title="Resume RAG Chatbot",
    page_icon="📄",
    layout="wide"
)


# -------------------------------------------------
# Title
# -------------------------------------------------

st.markdown(
    '<h1 class="main-title">Resume Intelligence Assistant</h1>',
    unsafe_allow_html=True
)

