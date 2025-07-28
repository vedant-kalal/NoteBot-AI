# 📁 File: modules/exam_question_predictor.py

from config.gemini_config import model

def generate_exam_questions(text):
    """
    Generate predicted exam questions from the given summarized or corrected note content.
    Returns a structured string (or JSON-style) output.
    """
    prompt = f"""
You are an expert in generating exam-style questions for students.

Based on the following study material, predict 5 important long-form or short-answer exam questions 
that are likely to be asked in a university exam. The questions should be concept-based, cover the core topics,
and should not be MCQs.

Be specific and clear.

Study Material:
\"\"\"
{text}
\"\"\"

Predicted Exam Questions:
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error generating questions: {e}"
