📚 NoteBot AI
NoteBot AI is a powerful AI-powered web application that lets you:

Upload handwritten or printed notes (PDF/PNG/JPG)

Extract and correct the text using Google Vision OCR

Summarize notes cleanly

Chat with your notes using a context-aware chatbot

Download clean summary PDFs and audio summaries

Export your chat history to PDF

✨ All powered by Google Gemini Pro (2.5) and Google Cloud Vision AI

🚀 Features
✅ 1. File Upload (PDF/PNG/JPG)
Upload scanned handwritten or printed notes

Supports PDFs and common image formats

Extracted using Google Cloud Vision OCR

✅ 2. OCR Text Correction
Automatically corrects OCR errors

Improves sentence structure and readability

✅ 3. Smart Summarization
Extracts important topics and structures

Organizes content using headers and key points

✅ 4. Audio Summary 🔊
Converts the cleaned summary to audio using free high-quality TTS

Supports math expressions and avoids reading markdown symbols like #, **, etc.

Downloadable MP3 format

✅ 5. Ask NoteBot 💬
Ask questions directly from your notes

NoteBot answers only within the uploaded content

Strictly avoids hallucinating out-of-scope answers

All chats are downloadable in a clean PDF format

🛠️ Tech Stack
Tool	Usage
Streamlit	Frontend Web UI
Google Vision API	OCR from scanned PDFs/images
Google Gemini Pro (2.5)	Summarization, Chatbot, Corrections
gTTS / pyttsx3 (configurable)	Text-to-Speech summary
fpdf	Generating downloadable PDFs

📁 Project Structure

The NoteBot/
├── app.py
├── config/
│   └── gemini_config.py
├── modules/
│   ├── ocr_extractor.py
│   ├── note_corrector.py
│   ├── summarizer.py
│   ├── chatbot.py
│   └── audio_generator.py
├── utils/
│   └── pdf_exporter.py
├── modules/
│   └── vision-key.json  # 🔑 Google Vision API key
├── README.md
└── requirements.txt 


🧠 How it Works
Upload scanned notes

OCR using Google Vision → Cleaned with Gemini

Choose to:

🔎 Summarize + Download PDF/MP3

🤖 Ask questions (AI chatbot trained only on your content)

Export chats or summaries anytime

📝 To-Do / Coming Soon
 Add MCQ Quiz Generator (temporarily removed)

 Real-time drawing board for handwritten notes

 AI-powered diagram explanation

