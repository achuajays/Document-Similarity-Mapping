# 📄 Document Review App with Gemini and ChromaDB

## 🌟 Overview

This project is an **AI-powered document review system** that analyzes and scores sections of uploaded documents against predefined templates. It leverages:

* **Google Gemini** for high-quality embeddings.
* **ChromaDB** for persistent vector storage and retrieval.
* **FastAPI** backend for efficient document processing.

🔍 It automates manual review by:

* **Detecting placeholder sections**
* **Checking semantic similarity to templates**
* **Generating contextual feedback**
* **Assigning an automatic decision** (APPROVE, CONDITIONAL REVIEW, REJECT)

---

## ✨ Features

* Store template instructions as embeddings in ChromaDB.
* Analyze documents section-by-section, comparing to templates.
* Detect unmodified placeholders or incomplete sections.
* Generate detailed feedback using Google Gemini.
* Configurable rules to enforce section requirements.
* Scalable to long, complex documents.

---

## 🗂 Directory Structure

```
document_review_app/
├── main.py               # FastAPI entry point, routes for document review
├── parsers.py            # Parses documents into sections and structures them
├── vector_store.py        # Handles ChromaDB vector database operations
├── similarity.py          # Computes semantic similarity scores using embeddings
├── placeholders.py        # Detects placeholders or unchanged text
├── rules.py               # Enforces section-level rules and required content
├── feedback.py            # Generates contextual feedback via Gemini
├── decision.py            # Makes final decision based on analysis
├── config.yaml            # Configuration file (Gemini keys, model, DB paths)
├── requirements.txt       # Python dependencies
└── utils.py               # Helper functions for parsing, embeddings, etc.
```

---

## 📂 Explanation of Files

* **`main.py`**
  Initializes the FastAPI app and defines routes (e.g., `/review`). Orchestrates document parsing, embedding, similarity checks, and decision-making.

* **`parsers.py`**
  Splits documents into sections (e.g., Introduction, Conclusion) based on formatting (Markdown, LaTeX, etc.). Prepares data for embedding.

* **`vector_store.py`**
  Interfaces with ChromaDB:

  * Adds template embeddings.
  * Retrieves similar sections for comparison.
  * Initializes and maintains persistent vector storage.

* **`similarity.py`**
  Calculates semantic similarity between document sections and templates using **cosine similarity** on embeddings.

* **`placeholders.py`**
  Detects incomplete or unchanged sections (e.g., `[Insert content here]`). Flags them for feedback.

* **`rules.py`**
  Defines validation rules (e.g., mandatory sections) and checks compliance.

* **`feedback.py`**
  Calls Google Gemini to generate **contextual feedback** for each section, using the template and actual content as context.

* **`decision.py`**
  Aggregates results from similarity, placeholders, and rules to determine the document’s final status:

  * `APPROVE`
  * `CONDITIONAL REVIEW`
  * `REJECT`

* **`config.yaml`**
  Stores configuration like Gemini API keys, model versions, ChromaDB paths, embedding settings, and similarity thresholds.

* **`requirements.txt`**
  Lists dependencies: `fastapi`, `uvicorn`, `chromadb`, `google-genai`, `scikit-learn`, `PyYAML`, etc.

* **`utils.py`**
  Utility functions: loading config, text cleaning, section formatting, logging.

---

## 🚀 Usage Instructions

### 1️⃣ Setup

1. **Clone the repository**:

```bash
git clone https://github.com/achuajays/Document-Similarity-Mapping.git
cd Document-Similarity-Mapping/document_review_app
```

2. **Create virtual environment**:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Configure the application**:

* Edit `config.yaml` with your **Google Gemini API key**, model name, ChromaDB path, and thresholds.

```yaml
gemini_api_key: "your_key_here"
gemini_embedding_model: "gemini-embedding-exp-03-07"
chromadb_path: "vector_store/"
similarity_threshold: 0.75
required_sections: ["Introduction", "Methodology", "Conclusion"]
```

5. **(Optional) Create `.env` for local environment variables**.

---

### 2️⃣ Initialize Template Embeddings

```python
python init_templates.py
```

This step **embeds templates** into ChromaDB, creating a reference for comparisons.

---

### 3️⃣ Run the App

```bash
uvicorn main:app --reload
```

Use the `/review` endpoint to upload documents.

---

### 4️⃣ Test with Diverse Demo Documents

* Place demo markdown files in `/demo_documents`.
* The system should output:

  * `APPROVE`: High similarity, no placeholders, complete.
  * `CONDITIONAL REVIEW`: Some issues but mostly valid.
  * `REJECT`: Low similarity, missing sections, placeholders detected.

---

## 🔧 Technical Details

* **LLM**: Google Gemini (`genai` library) for embeddings and feedback.
* **Vector DB**: ChromaDB with persistent storage.
* **Backend**: FastAPI, async-friendly.
* **Dependencies**: FastAPI, Uvicorn, ChromaDB, Google GenAI, scikit-learn, PyYAML.
* **Language**: Python 3.10+

---

## 🤝 Contributing

* **Report issues**: Use GitHub Issues.
* **Fork & PR**: Add features or fix bugs with clear commits.
* **Coding style**: Follow PEP8 and include docstrings.

---

## 📄 License

Licensed under the **MIT License**. See `LICENSE` for details.

---

## 🙏 Acknowledgments

* **Google Gemini** for embeddings and generative feedback.
* **ChromaDB** for scalable vector storage.
* **FastAPI** for the async web backend.


