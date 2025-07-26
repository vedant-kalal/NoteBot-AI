from fpdf import FPDF
import re
from io import BytesIO

def clean_text(text):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map
        u"\U0001F1E0-\U0001F1FF"  # flags
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def export_summary_to_pdf(summary_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    clean_summary = clean_text(summary_text)
    for line in clean_summary.split('\n'):
        pdf.multi_cell(0, 10, line)

    pdf_data = pdf.output(dest='S').encode('latin-1')  # Return string as bytes
    return pdf_data

def export_chat_to_pdf(chat_history):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for idx, (q, a) in enumerate(chat_history):
        clean_q = clean_text(q)
        clean_a = clean_text(a)
        pdf.multi_cell(0, 10, f"Q{idx+1}: {clean_q}")
        pdf.multi_cell(0, 10, f"A{idx+1}: {clean_a}")
        pdf.ln()

    pdf_data = pdf.output(dest='S').encode('latin-1')
    return pdf_data
