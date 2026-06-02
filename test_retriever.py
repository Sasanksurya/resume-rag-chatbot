from embeddings import get_embeddings
from retriever import load_vector_store

embeddings = get_embeddings()

db = load_vector_store(embeddings)

query = "What machine learning projects has he done?"

results = db.similarity_search(query, k=3)

for i, doc in enumerate(results):
    print(f"\nResult {i+1}")
    print("-" * 50)
    print(doc.page_content)