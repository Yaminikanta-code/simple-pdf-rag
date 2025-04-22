from load_pdf import load_documents
from split_text import split_documents
from embedder import get_embedder
from vector_store import create_vector_store, load_vector_store
from retriever import get_similar_documents

def main():
    documents = load_documents()
    split_docs = split_documents(documents)
    embedder = get_embedder()

    # Comment out this line if vector store is already created
    create_vector_store(split_docs, embedder)

    retriever = load_vector_store(embedder)
    result = get_similar_documents(retriever, "What is FS Module?")
    print("Relevant Chunks:", result)

if __name__ == "__main__":
    main()
