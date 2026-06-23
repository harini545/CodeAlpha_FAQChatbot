import pandas as pd
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load FAQ dataset
faq_data = pd.read_csv("faq.csv")

questions = faq_data["question"]
answers = faq_data["answer"]

# English stopwords
stop_words = set(stopwords.words("english"))


# Text preprocessing
def preprocess(text):
    text = str(text).lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]
    return " ".join(words)


# Preprocess all questions
processed_questions = questions.apply(preprocess)

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(processed_questions)


# Chatbot Function
def get_answer(user_question):

    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening",
    ]

    if user_question.lower().strip() in greetings:
        return (
            "👋 Hello! I'm your Python FAQ Chatbot.\n\nAsk me anything about Python programming!",
            1.0,
        )

    processed_question = preprocess(user_question)

    user_vector = vectorizer.transform([processed_question])

    similarity = cosine_similarity(user_vector, question_vectors)

    best_match = similarity.argmax()

    confidence = similarity[0][best_match]

    if confidence < 0.30:
        return (
            """🤔 Sorry, I couldn't find a suitable answer.

Try asking about:

• Python
• Variables
• Lists
• Tuples
• Dictionaries
• Loops
• Functions
• Classes
• OOP
• Machine Learning
• Streamlit
""",
            confidence,
        )

    return answers.iloc[best_match], confidence