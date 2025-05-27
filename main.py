from fastapi import FastAPI, UploadFile, File
from parsers import parse_document
from vector_store import get_template_vectors
from similarity import compare_sections
from placeholders import check_placeholders
from rules import enforce_rules
from feedback import generate_feedback
from decision import make_decision

app = FastAPI()

@app.post("/review")
async def review_document(file: UploadFile = File(...)):
    # 1. Parse uploaded document
    sections = await parse_document(file)

    # 2. Load template vectors from ChromaDB
    template_vectors = get_template_vectors()

    # 3. Compare sections with templates
    similarity_scores = compare_sections(sections, template_vectors)

    # 4. Check for unchanged placeholders
    placeholders_flags = check_placeholders(sections)

    # 5. Enforce SME rules
    rules_status = enforce_rules(sections, similarity_scores)

    # 6. Generate LLM feedback (Google Gemini)
    feedback = generate_feedback(sections)

    # 7. Make final decision
    decision = make_decision(similarity_scores, placeholders_flags, rules_status, feedback)

    return {
        "similarity_scores": similarity_scores,
        "placeholders": placeholders_flags,
        "rules_status": rules_status,
        "feedback": feedback,
        "final_decision": decision
    }
