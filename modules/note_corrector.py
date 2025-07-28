# 📁 File: modules/note_corrector.py

from config.gemini_config import model

def correct_text(ocr_text):
    prompt = f"""
You are a smart AI assistant. The following text has been extracted using OCR and may contain errors such as misrecognized characters, punctuation issues, or broken words.

Your job is to correct the OCR errors and return clean, well-structured, readable content without changing the original meaning.

Text to correct:
\"\"\"
{ocr_text}
\"\"\"

Return only the corrected version of the text.
"""
    response = model.generate_content(prompt)
    return response.text.strip()
