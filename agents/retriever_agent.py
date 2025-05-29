from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Sample knowledge base
documents = [
    "TSMC Q1 earnings beat expectations by 4%",
    "Samsung missed earnings by 2% in Q1",
    "Asia tech allocation increased from 18% to 22% of AUM",
    "Yields in Asia are rising, causing caution in markets",
]

model = SentenceTransformer("all-MiniLM-L6-v2")
doc_embeddings = model.encode(documents)

index = faiss.IndexFlatL2(len(doc_embeddings[0]))
index.add(np.array(doc_embeddings))

def retrieve(query, top_k=2):
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), top_k)
    return [documents[i] for i in I[0]]
