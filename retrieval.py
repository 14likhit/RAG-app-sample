from sentence_transformers import SentenceTransformer
import chromadb

# Load Embedding Model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
chroma_client = chromadb.PersistentClient(path="./vector_storage")
collection = chroma_client.get_collection(name="documents")

def retrieve_relevant_docs(query, top_k=2):
    query_vector = embedding_model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_vector], n_results=top_k)
    
    retrieved_docs = [item["text"] for item in results["metadatas"][0]]
    return retrieved_docs

