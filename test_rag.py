from embeddings import get_embeddings
from rag_chain import get_answer

embeddings = get_embeddings()

question = "What machine learning projects has he worked on?"

answer = get_answer(
    question,
    embeddings
)

print("\nAnswer:")
print(answer)