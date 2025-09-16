from User import User
from google import genai

class AI:
    def __init__(self, model):
        self.model = model
        self.client = genai.Client()
        self.chat = self.client.chats.create(model=model)

    def chatSession(self, message):
        # formatted = [f"{m['role'].upper()}:{m['content']}" for m in messages]
        response = self.chat.send_message(message)
        return response.text
    
if __name__ == "__main__":
    u = User('Efe Kwode', 'Junior Machine Learning Engineer', ['SQL', 'Numpy', 'Spark', 'Scikit-Learn', 'NLP with Hugging Face'])
    gemini = AI("gemini-2.5-pro")
    interview = gemini.chatSession(f'''You are an AI interview coach. Your role is to simulate a realistic interview for the candidate based on their background and target job role.  

Rules:
- Ask one question at a time (either technical or behavioral).
- Wait for the candidate’s answer before moving to the next question.
- After each answer, provide constructive feedback:
  - Highlight strengths.
  - Point out missing details or mistakes.
  - Suggest how to improve the response (e.g., STAR format for behavioral answers).
- Keep feedback concise, professional, and encouraging.
- Ask 3–5 questions in total per session.
- At the end, give a summary report with:
  - Strengths
  - Weaknesses
  - Overall score (out of 10). This is the Candidate {u.stuff()}''')
    print(interview)