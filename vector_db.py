import chromadb
from sentence_transformers import SentenceTransformer

# Load Embedding Model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize Vector Database (Persistent Storage)
chroma_client = chromadb.PersistentClient(path="./vector_storage")
collection = chroma_client.get_or_create_collection(name="documents")

def store_documents():
    documents = [
        "The Eiffel Tower is located in Paris.",
        "Mount Everest is the tallest mountain in the world.",
        "Python is a popular programming language.",
        "The Amazon Rainforest is the largest rainforest on Earth.",
    ]

    for i, doc in enumerate(documents):
        vector = embedding_model.encode(doc).tolist()
        collection.add(ids=[str(i)], embeddings=[vector], metadatas=[{"text": doc}])

    print("✅ Documents stored in vector database!")

if __name__ == "__main__":
    store_documents()
