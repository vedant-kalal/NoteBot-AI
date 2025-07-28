# 📁 File: modules/audio_generator.py

from gtts import gTTS
from io import BytesIO
from config.gemini_config import model

def make_text_speech_friendly(summary_text):
    """
    Uses Gemini to rewrite the summary in a way that sounds natural when spoken.
    Removes headers, markdown, math symbols, and rephrases awkward sentences.
    """

    prompt = f"""
You are a voice assistant preparing a summary for spoken output.
dont speak the unnecery things like a ofcourse here is the summary or something like that.
start with speaking here is the summary of the (speak name of the topic or if there is no topic found then speak word "notes" instead of "topic name") and then start speaking the summary(without any additional commentary).
dont sound robotic or like a computer.
user should feel like he is listening to a human voice.
The following text is an AI-generated summary of notes. Please rewrite it in a way that sounds natural when spoken aloud by a voice AI.

- Remove or rephrase markdown symbols like **, #, etc.
- Reword or skip any mathematical expressions like asterisk (*), slash (/), plus (+), or minus (-) so they don't sound robotic.
- Ensure everything is easy to listen to and sounds like natural spoken English.

Summary:
\"\"\"
{summary_text}
\"\"\"

Speak-friendly version:
"""
    response = model.generate_content(prompt)
    return response.text.strip()

def text_to_speech_audio(summary_text):
    speech_friendly_text = make_text_speech_friendly(summary_text)
    tts = gTTS(speech_friendly_text, lang='en')
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return mp3_fp
