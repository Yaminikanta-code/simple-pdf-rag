from langchain_qdrant import QdrantVectorStore
from langchain_core.documents import Document
from config import QDRANT_URL, COLLECTION_NAME


def create_vector_store(documents, embedder):
    return QdrantVectorStore.from_documents(
        documents=documents,
        url=QDRANT_URL,
        collection_name=COLLECTION_NAME,
        embedding=embedder
    )


def load_vector_store(embedder):
    return QdrantVectorStore.from_existing_collection(
        url=QDRANT_URL,
        collection_name=COLLECTION_NAME,
        embedding=embedder
    )


# C: Add documents
def add_documents(vector_store, documents):
    vector_store.add_documents(documents)


# R: Retrieve similar documents
def search_documents(vector_store, query, k=4):
    return vector_store.similarity_search(query=query, k=k)


# U: Update documents (delete + re-add with same ids or metadata)
def update_document(vector_store, document_id, new_document: Document):
    vector_store.delete(ids=[document_id])
    vector_store.add_documents([new_document])


# D: Delete by ID or filter
def delete_document_by_id(vector_store, document_id):
    vector_store.delete(ids=[document_id])


def delete_documents_by_filter(vector_store, filter_dict):
    vector_store.delete(filter=filter_dict)
