from User import User
from google import genai

class AI:
    def __init__(self, model):
        self.model = model
        self.client = genai.Client()

    def interviewSession(self, prompt: str):
        response = self.client.models.generate_content(
            model = self.model,
            contents = prompt
        )
        return response.text
    
if __name__ == "__main__":
    u = User('Efe Kwode', 'Junior Machine Learning Engineer', ['SQL', 'Numpy', 'Spark', 'Scikit-Learn', 'NLP with Hugging Face'])
    prompt = u.prompt()
    gemini = AI("gemini-2.5-flash")
    interview = gemini.interviewSession(prompt=prompt)
    print(interview)