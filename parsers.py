import re
from PyPDF2 import PdfReader
from docx import Document

async def parse_document(file):
    content = ""
    if file.filename.endswith('.pdf'):
        reader = PdfReader(file.file)
        for page in reader.pages:
            content += page.extract_text()
    elif file.filename.endswith('.docx'):
        doc = Document(file.file)
        for para in doc.paragraphs:
            content += para.text + "\n"
    else:
        content = (await file.read()).decode()

    # Simple header-based section splitting
    sections = re.split(r'\n\s*(\d+\.\s+[^\n]+)', content)
    return {f"Section {i}": text for i, text in enumerate(sections) if text.strip()}
