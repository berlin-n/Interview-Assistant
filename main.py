from AI import AI, User

gemini = AI("gemini-2.5-flash")
user1 = User("Efe Kwode", "Junior Machine Learning Engineer", ['SQL', 'Numpy', 'Spark', 'Scikit-Learn', 'NLP with Hugging Face'])
prompt = user1.prompt()
interview = gemini.chat([])
print(interview)