# 📁 File: modules/summarizer.py

from config.gemini_config import model

def summarize_notes(text):
    prompt = f"""
You are a smart assistant. Summarize the following notes clearly, highlighting topics and key points.
If formulas or topics are found, organize them under headers.it should directly address the content without unnecessary preamble without any additional commentary.it should add the title of the notes at the top of the summary.

Notes:
\"\"\"
{text}
\"\"\"
"""
    response = model.generate_content(prompt)
    return response.text.strip()
