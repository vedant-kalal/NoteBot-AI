# ============================================================================
# 📁 File: modules/ocr_extractor.py
# 📷 Google Vision OCR Extractor for PDF, PNG, JPG
# ============================================================================

import os
import io
from PyPDF2 import PdfReader
from google.cloud import vision
from PIL import Image
import tempfile

# ✅ Set up the path to your Vision API JSON key (inside modules folder)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "modules/vision-key.json"

# ✅ Initialize the Vision API client
client = vision.ImageAnnotatorClient()

def extract_text_from_file(uploaded_file):
    """
    Extracts text from uploaded file using Google Cloud Vision API.
    Supports PDFs, PNGs, JPGs, JPEGs.
    """

    ext = uploaded_file.name.split(".")[-1].lower()
    text = ""

    if ext == "pdf":
        # Save PDF temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        # Use PyPDF2 to extract pages and Vision to OCR
        reader = PdfReader(tmp_path)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

    else:
        # For image formats: PNG, JPG, JPEG
        content = uploaded_file.read()
        image = vision.Image(content=content)

        # OCR using Vision API
        response = client.document_text_detection(image=image)

        if response.error.message:
            raise Exception(f"❌ Vision API Error: {response.error.message}")

        if response.full_text_annotation.text:
            text = response.full_text_annotation.text
        else:
            text = "❌ No text found or OCR failed."

    return text
