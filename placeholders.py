import re

def check_placeholders(sections):
    pattern = re.compile(r'\{\{.*?\}\}|TBD|INSERT|PLACEHOLDER', re.IGNORECASE)
    return {sec: bool(pattern.search(text)) for sec, text in sections.items()}
