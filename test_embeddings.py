from embeddings import get_embeddings

embeddings = get_embeddings()

vector = embeddings.embed_query(
    "Customer Churn Prediction"
)

print("Vector Length:", len(vector))

print(vector[:10])