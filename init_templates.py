import chromadb
from google import genai
from config import gemini
# Initialize Google Gemini client
client = genai.Client(api_key=gemini)

# Sample template sections (replace with your actual templates)
template_sections = [
    {
        "section_id": "template-1",
        "section_title": "1. Introduction",
        "section_text": "This section provides an overview of the technical document, outlining objectives and scope."
    },
    {
        "section_id": "template-2",
        "section_title": "2. Functional Requirements",
        "section_text": "This section details the functional specifications, including use cases and system behavior."
    },
    {
        "section_id": "template-3",
        "section_title": "3. Technical Architecture",
        "section_text": "This section describes the system architecture, components, and interactions."
    },
    {
        "section_id": "template-4",
        "section_title": "4. Compliance and Standards",
        "section_text": "This section outlines compliance with regulatory standards and internal policies."
    }
]

# Initialize ChromaDB persistent client
chroma_client = chromadb.PersistentClient(path="chroma_db")
collection = chroma_client.get_or_create_collection("document_templates")

# Add templates to ChromaDB
for template in template_sections:
    print(f"Processing {template['section_title']}...")

    # Generate embedding using Gemini
    result = client.models.embed_content(
        model="gemini-embedding-exp-03-07",
        contents=template["section_text"]
    )
    embedding = result.embeddings[0].values
    # Add to ChromaDB
    collection.add(
        embeddings=[embedding],
        metadatas=[{
            "section_id": template["section_id"],
            "section_title": template["section_title"]
        }],
        ids=[template["section_id"]]
    )

print("✅ Template sections added to ChromaDB!")
