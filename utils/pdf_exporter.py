from fpdf import FPDF
from io import BytesIO
import os

# Font paths
FONT_DIR = "data"
FONT_REGULAR = os.path.join(FONT_DIR, "DejaVuSans.ttf")
FONT_BOLD = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")

class PDFExporter(FPDF):
    def __init__(self, title="NoteBot PDF"):
        super().__init__()
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
        self.set_title(title)

        if os.path.exists(FONT_REGULAR):
            self.add_font("DejaVu", '', FONT_REGULAR, uni=True)
        if os.path.exists(FONT_BOLD):
            self.add_font("DejaVu", 'B', FONT_BOLD, uni=True)

        # Default font if DejaVu exists
        if os.path.exists(FONT_REGULAR):
            self.set_font("DejaVu", size=12)
        else:
            self.set_font("Arial", size=12)

    def write_text(self, text):
        for line in text.split('\n'):
            self.multi_cell(0, 10, line)

# Export summary as PDF
def export_summary_to_pdf(summary_text):
    pdf = PDFExporter(title="Summarized Notes")
    pdf.set_font("DejaVu", size=12)
    pdf.write_text(summary_text)
    buffer = BytesIO()
    pdf.output(buffer, 'S').encode('latin-1')  # Return string as bytes
    buffer.write(pdf.output(dest='S').encode('latin-1'))
    buffer.seek(0)
    return buffer

# Export chat as PDF
def export_chat_to_pdf(chat_history):
    pdf = PDFExporter(title="Chat History")
    for i, (question, answer) in enumerate(chat_history, start=1):
        pdf.set_font("DejaVu", size=12, style="B")
        pdf.multi_cell(0, 10, f"Q{i}: {question}")
        pdf.set_font("DejaVu", size=12)
        pdf.multi_cell(0, 10, f"A{i}: {answer}")
        pdf.ln()
    buffer = BytesIO()
    buffer.write(pdf.output(dest='S').encode('latin-1'))
    buffer.seek(0)
    return buffer
