from pdf_loader import extract_text_from_pdf
from chunking import create_chunks
from embeddings import get_embeddings
from vector_store import create_vector_store

text = extract_text_from_pdf("data/resume.pdf")

chunks = create_chunks(text)

embeddings = get_embeddings()

vector_store = create_vector_store(
    chunks,
    embeddings
)

print("FAISS Index Created Successfully")