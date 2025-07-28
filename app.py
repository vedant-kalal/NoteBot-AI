# 📁 File: app.py  (Updated Streamlit WebApp with Separated Panels)

import streamlit as st
from modules.ocr_extractor import extract_text_from_file
from modules.note_corrector import correct_text
from modules.summarizer import summarize_notes
from modules.chatbot import NoteBot
from modules.audio_generator import text_to_speech_audio
from modules.exam_question_predictor import generate_exam_questions
import os
from io import BytesIO
import streamlit.components.v1 as components
import re

# Delay PDF import to avoid circular import error
exporters = None
def lazy_load_exporters():
    global exporters
    if exporters is None:
        from utils import pdf_exporter
        exporters = pdf_exporter

def clean_summary_for_export(summary_text):
    cleaned = re.sub(r'\*\*(.*?)\*\*', r'\1', summary_text)  # Remove bold ** **
    cleaned = re.sub(r'# +', '', cleaned)  # Remove markdown headers
    return cleaned

st.set_page_config(page_title="NoteBot AI", layout="wide")
st.markdown("""
    <h1 style='font-size: 40px;'>📚 NoteBot AI</h1>
    <p style='font-size: 22px;'>Upload notes (PDF/PNG/JPG), get summaries, chat with NoteBot, predict exam questions, and download as PDF or audio!</p>
""", unsafe_allow_html=True)

# State Initialization
for key, val in {
    'ocr_text': None,
    'corrected_text': None,
    'notebot': None,
    'history': [],
    'summary': None,
    'summarize_expanded': False,
    'loading': False,
    'last_uploaded_filename': None,
    'file_uploaded': False,
    'exam_questions': None
}.items():
    if key not in st.session_state:
        st.session_state[key] = val

def disable_all_buttons():
    st.session_state.loading = True

# Sidebar History
with st.sidebar:
    st.header("📜 Chat History")
    to_delete = None
    if st.session_state.history:
        for i, (q, a) in enumerate(st.session_state.history):
            with st.expander(f"Q{i+1}: {q[:30]}..."):
                st.markdown(f"**Q:** {q}")
                st.markdown(f"**A:** {a}")
                if st.button(f"❌ Delete Q{i+1}", key=f"del_{i}"):
                    to_delete = i
        if to_delete is not None:
            st.session_state.history.pop(to_delete)
            st.rerun()
        if st.button("🗑️ Clear All History"):
            st.session_state.history = []
            st.rerun()

# Upload File
new_upload = st.file_uploader("Upload your notes (PDF, PNG, JPG)", type=["pdf", "png", "jpg", "jpeg"])

if new_upload is None and st.session_state.last_uploaded_filename is not None:
    for key in ['ocr_text', 'corrected_text', 'notebot', 'summary', 'exam_questions', 'history', 'summarize_expanded', 'last_uploaded_filename']:
        st.session_state[key] = None if key not in ['history'] else []
    st.session_state.file_uploaded = False
    st.rerun()

elif new_upload and (new_upload.name != st.session_state.last_uploaded_filename):
    with st.spinner("Extracting and correcting notes..."):
        raw_text = extract_text_from_file(new_upload)
        st.session_state.ocr_text = raw_text
        st.session_state.corrected_text = correct_text(raw_text)
        st.session_state.notebot = None
        st.session_state.summary = None
        st.session_state.exam_questions = None
        st.session_state.history = []
        st.session_state.summarize_expanded = False
        st.session_state.last_uploaded_filename = new_upload.name
        st.session_state.file_uploaded = True
    st.success("✅ Notes processed and saved!")

if st.session_state.corrected_text:
    # --- Summarizer Panel ---
    with st.expander("📄 Summarized Notes", expanded=True):
        if st.button("Summarize Notes", disabled=st.session_state.loading):
            disable_all_buttons()
            with st.spinner("🔄 Summarizing your notes..."):
                st.session_state.summary = summarize_notes(st.session_state.corrected_text)
                st.session_state.summarize_expanded = True
                st.session_state.loading = False

        if st.session_state.summary:
            st.markdown("### ✨ Summary")
            st.write(st.session_state.summary)
            lazy_load_exporters()
            cleaned_summary = clean_summary_for_export(st.session_state.summary)
            pdf_file = exporters.export_summary_to_pdf(cleaned_summary)
            st.download_button("📥 Download Summary PDF", data=pdf_file, file_name="summary.pdf", mime="application/pdf")

    # --- Audio Summary Panel ---
    if st.session_state.summary:
        with st.expander("🔊 Listen to Audio Summary", expanded=False):
            if st.button("Generate Audio Summary", key="audio_button"):
                with st.spinner("🔄 Generating audio summary..."):
                    cleaned_summary = clean_summary_for_export(st.session_state.summary)
                    st.session_state.audio_file = text_to_speech_audio(cleaned_summary)

            if st.session_state.get("audio_file") is not None:
                st.audio(st.session_state.audio_file, format="audio/mp3")
                st.download_button("🎷 Download Audio Summary", data=st.session_state.audio_file, file_name="summary.mp3", mime="audio/mpeg")

    # --- Exam Questions Panel ---
    if st.session_state.summary:
        with st.expander("📌 Predicted Exam Questions", expanded=False):
            if st.button("📑 Generate Exam Questions", key="exam_button"):
                with st.spinner("🔍 Predicting exam questions..."):
                    st.session_state.exam_questions = generate_exam_questions(cleaned_summary)

            if st.session_state.exam_questions:
                st.markdown("### 📝 Likely Exam Questions")
                st.code(st.session_state.exam_questions, language="text")

    # --- Chatbot Panel ---
    with st.expander("💬 Chat with NoteBot", expanded=False):
        if st.session_state.notebot is None:
            st.session_state.notebot = NoteBot(context=st.session_state.corrected_text)
        st.markdown("**Hi, I'm NoteBot – here to assist you with your uploaded notes.**")
        user_query = st.text_input("Ask a question about your notes", key="chat_input")
        if user_query:
            with st.spinner("🤖 Generating answer..."):
                answer = st.session_state.notebot.chat(user_query)
                st.session_state.history.append((user_query, answer))
                st.markdown(f"**You:** {user_query}")
                st.markdown(f"**NoteBot:** {answer}")
        if st.session_state.history:
            lazy_load_exporters()
            pdf_file = exporters.export_chat_to_pdf(st.session_state.history)
            st.download_button("📥 Download Chat PDF", data=pdf_file, file_name="chat.pdf", mime="application/pdf")
