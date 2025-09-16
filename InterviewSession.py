from AI import AI
from User import User

class InterviewSession:
    def __init__(self, ai: AI, user:User):
        self.ai = ai
        self.finished = False
        self.user = user
        self.prompt = f'''You are an AI interview coach. Your role is to simulate a realistic interview for the candidate based on their background and target job role.  

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
  - Overall score (out of 10). This is the Candidate {user.stuff()}'''

    def start(self):
        ai_response = self.ai.chatSession(self.prompt)
        print("Starting Interview Session...")

        while not self.finished:
            print(f"AI : {ai_response}")
            answer = input("Your Answer:")
            print("AI is thinking...")
            ai_response = self.ai.chatSession(answer)
            
    
if __name__=="__main__":
    u = User('Efe Kwode', 'Junior Machine Learning Engineer', ['SQL', 'Numpy', 'Spark', 'Scikit-Learn', 'NLP with Hugging Face'])
    newInterview = InterviewSession(AI("gemini-2.5-flash"),u)
    newInterview.start()