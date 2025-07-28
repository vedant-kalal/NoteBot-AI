# 📁 File: modules/chatbot.py

from config.gemini_config import model

class NoteBot:
    def __init__(self, context):
        self.context = context
        self.history = []

    def chat(self, user_query):
        prompt = f"""
You are NoteBot, an assistant who only answers questions based on the following notes.

If a question is out of scope (not related to the notes), politely respond:
"I'm NoteBot, designed to assist only with the uploaded notes."

Notes:
\"\"\"
{self.context}
\"\"\"

Question:
{user_query}

Answer:
"""
        response = model.generate_content(prompt)
        answer = response.text.strip()
        self.history.append((user_query, answer))
        return answer
