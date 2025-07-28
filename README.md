🧠 NoteBot AI – Intelligent Note Evaluator, Summarizer & Chatbot
🏆 Hackathon Winning Project – RotaHack 2025 (New LJ College)
A complete AI-powered platform for scanning handwritten notes, summarizing them, generating audio, predicting exam questions, and interacting via chatbot.

📌 Project Overview
NoteBot AI is an educational assistant web app that transforms scanned handwritten or printed notes into structured, summarized, and interactable content using AI. It enables students and teachers to:

Extract handwritten content using OCR 

Automatically correct grammar without altering meaning

Summarize lengthy notes

Convert summaries to speech

Predict exam questions based on your notes

Chat with a smart bot trained only on your uploaded content

Download summaries and chats as PDFs/audio

🚀 Live Features
✅ Upload PDF/PNG/JPG scanned notes
✅ Handwriting OCR via Google Vision API
✅ Grammatical Correction using Gemini AI
✅ Summarization into clear, formatted text
✅ Audio Summary using gTTS
✅ Exam Question Prediction from uploaded notes
✅ NoteBot Chat (Context-locked chatbot – no hallucinations)
✅ Download PDF & MP3 of outputs
✅ Buffering & UI feedback for long operations

🛠️ Tech Stack
Frontend:

Streamlit (Python Web App UI)

HTML + Streamlit components

Backend / AI Services:

Google Vision API – for OCR

Gemini 1.5 Pro – for grammar, summarization, Q&A, exam prediction

Python

PDF & Audio Processing:

FPDF, ReportLab – for PDF generation

gTTS – for text-to-speech

PIL, PyPDF2 – for image/PDF handling

regex – for text cleaning

📁 Project Structure
bash
Copy
Edit
📦 NoteBotAI/
├── app.py                      # Main Streamlit app

├── modules/
│   ├── ocr_extractor.py  # OCR using Google Vision API

│   ├── note_corrector.py      # Grammar correction with Gemini

│   ├── summarizer.py          # Summarization using Gemini

│   ├── audio_generator.py     # Text-to-speech

│   ├── chatbot.py             # NoteBot chat logic

│   └── exam_question_predictor.py # AI-generated questions

├── utils/
│   └── pdf_exporter.py        # PDF generation utilities

├── data/
│   └── DejaVuSans.ttf         # Font file for PDF export
└── requirements.txt

🧠 How It Works
Upload File: Upload scanned handwritten/typed notes as image or PDF

OCR + Correction: Extract text using Google Vision, then correct it with Gemini

Summarize: Generate AI summary and download as PDF

Generate Audio: Convert summary to audio (MP3) with gTTS

Predict Questions: AI predicts possible exam questions from the summary

Chat with Notes: Ask anything from uploaded content using NoteBot

Export Everything: Get summaries and chats in downloadable formats

🔒 Why It’s Better Than General Tools
🔐 No hallucinations – Chat only uses your uploaded content

✍️ Handwriting support – far better OCR + grammar integration than ChatGPT

📚 Exam-focused – auto predicts questions from actual content

🧑‍🏫 Teacher & Student Friendly – fair, fast, and transparent evaluation

💾 Offline friendly – all generated data is downloadable

🏆 Achievement
🥇 1st Prize – RotaHack 2025 Hackathon
Organized by the Rotaract Club of New LJ College – recognized for innovation, utility, and real-world applicability in education technology.

📦 Installation Guide
bash
Copy
Edit
git clone https://github.com/vedant-kalal/notebot-ai.git
cd notebot-ai
pip install -r requirements.txt
streamlit run app.py
⚠️ Prerequisites
Google Cloud Vision API Key (store as JSON and set via environment or code)
Gemini API Access (gemini-1.5-pro)

🧪 Demo
👉 [https://video-link-generator.replit.app/v/k9fb6vcmprlb8up9h8blyv]
🧑‍💻 Or deploy via platforms like Streamlit Cloud or Render

