from langchain_openai import OpenAIEmbeddings
from config import OPENAI_API_KEY, EMBED_MODEL

def get_embedder():
    return OpenAIEmbeddings(model=EMBED_MODEL, api_key=OPENAI_API_KEY)
