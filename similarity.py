from google import genai
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from config import gemini

client = genai.Client(api_key=gemini)


def compare_sections(sections, template_vectors):
    scores = {}
    for sec_name, text in sections.items():
        # Get embedding from Gemini, extract first embedding's values list
        embedding_obj = client.models.embed_content(
            model="gemini-embedding-exp-03-07",
            contents=text
        ).embeddings[0]  # first ContentEmbedding object

        embedding = embedding_obj.values  # list of floats

        best_match = None
        highest_score = 0
        for template_emb_obj, meta in zip(template_vectors['embeddings'], template_vectors['metadatas']):
            # Extract values if template_emb_obj is ContentEmbedding
            template_emb = template_emb_obj.values if hasattr(template_emb_obj, "values") else template_emb_obj

            score = cosine_similarity([embedding], [template_emb])[0][0]
            if score > highest_score:
                highest_score = score
                best_match = meta.get("section")
        scores[sec_name] = {"best_match": best_match, "similarity": highest_score}
    return scores
