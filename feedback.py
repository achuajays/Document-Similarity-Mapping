from google import genai
from config import gemini

genai_client = genai.Client(api_key=gemini)

def generate_feedback(sections):
    feedback = {}
    for sec, text in sections.items():
        prompt = f"Review the following document section and provide improvement suggestions:\n\n{text}"
        response = genai_client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[prompt]
        )
        feedback[sec] = response.text
    return feedback
