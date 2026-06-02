from langchain_community.vectorstores import FAISS

def load_vector_store(embeddings):

    db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db