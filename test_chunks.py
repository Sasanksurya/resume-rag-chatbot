from pdf_loader import extract_text_from_pdf
from chunking import create_chunks

text = extract_text_from_pdf("data/resume.pdf")

chunks = create_chunks(text)

print("Total Chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print("-"*50)
    print(chunk)