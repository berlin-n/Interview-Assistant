class User:
    def __init__(self, name: str, role: str, skills: list[str]):
        self.name = name
        self.role = role
        self.skills = skills


    def stuff(self):
        text = f'''
Candidate Profile:
Name: {self.name}
Target Role: {self.role}
Skills: {self.skills}

Begin the interview now by greeting the candidate and asking the first question.'''

        return text

if __name__ == '__main__':
    u = User('Efe Kwode', 'Junior Machine Learning Engineer', ['SQL', 'Numpy', 'Spark', 'Scikit-Learn', 'NLP with Hugging Face'])
    print(u.stuff())
