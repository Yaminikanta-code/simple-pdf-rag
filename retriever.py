def get_similar_documents(retriever, query):
    return retriever.similarity_search(query=query)
