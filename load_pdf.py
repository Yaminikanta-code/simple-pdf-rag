from langchain_community.document_loaders import PyPDFLoader
from config import PDF_PATH

def load_documents():
    loader = PyPDFLoader(file_path=PDF_PATH)
    return loader.load()
