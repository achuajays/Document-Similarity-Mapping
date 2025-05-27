import chromadb
from google import genai
from config import gemini
client = genai.Client(api_key=gemini )

def get_template_vectors():
    chroma_client = chromadb.PersistentClient(path="chroma_db")
    collection = chroma_client.get_collection("document_templates")
    results = collection.get(include=["embeddings", "metadatas"])
    return results

def add_template_to_db(section_text, metadata):
    embedding = client.models.embed_content(
        model="gemini-embedding-exp-03-07",
        contents=section_text
    ).embeddings
    chroma_client = chromadb.PersistentClient(path="chroma_db")
    collection = chroma_client.get_or_create_collection("document_templates")
    collection.add(
        embeddings=[embedding],
        metadatas=[metadata],
        ids=[metadata["section_id"]]
    )
