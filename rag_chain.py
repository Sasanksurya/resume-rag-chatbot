
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS

load_dotenv()


def get_answer(question, embeddings):

    # Load FAISS Vector Store
    db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Retrieve Relevant Chunks
    docs = db.similarity_search(
        question,
        k=3
    )

    # Create Context
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # Initialize Groq LLM
    llm = ChatGroq(
        model_name="llama-3.1-8b-instant",
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    # Prompt Template
    prompt = f"""
    You are a Resume Assistant.

    Rules:
    1. Answer only from the provided resume context.
    2. If information is not available, say:
       "I could not find that information in the resume."
    3. Keep answers professional and concise.

    Resume Context:
    {context}

    Question:
    {question}

    Answer:
    """

    # Generate Response
    response = llm.invoke(prompt)

    # Return Answer + Retrieved Chunks
    return response.content, docs

