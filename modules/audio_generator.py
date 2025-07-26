# 📁 File: modules/audio_generator.py

from gtts import gTTS
from io import BytesIO
import re

def clean_text_for_speech(text: str) -> str:
    """
    Pre-process text to improve speech synthesis:
    - Removes markdown symbols (like ##)
    - Converts math-like expressions to natural phrases
    """

    # Replace Markdown-style headers (##, ###) with just the title
    text = re.sub(r'#+\s*', '', text)

    # Replace common math expressions
    text = re.sub(r'(\w+)\s*=\s*(\w+)\s*\^\s*(\d+)', r'\1 equals \2 to the power of \3', text)
    text = re.sub(r'(\w+)\s*=\s*(\w+)\s*/\s*(\w+)', r'\1 equals \2 divided by \3', text)
    text = re.sub(r'(\w+)\s*=\s*(\w+)\s*\*\s*(\w+)', r'\1 equals \2 multiplied by \3', text)
    text = text.replace('=', ' equals ')
    text = text.replace('+', ' plus ')
    text = text.replace('-', ' minus ')
    text = text.replace('*', ' multiplied by ')
    text = text.replace('/', ' divided by ')
    text = text.replace('^', ' to the power of ')

    return text


def text_to_speech_audio(text: str) -> BytesIO:
    """
    Converts the given cleaned text to speech and returns a BytesIO object with MP3 audio.
    """
    cleaned = clean_text_for_speech(text)
    if not cleaned.strip():
        raise ValueError("No valid text provided for speech synthesis.")

    tts = gTTS(cleaned, lang='en')
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes
