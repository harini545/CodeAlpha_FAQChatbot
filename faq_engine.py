import pandas as pd
from embeddings import SemanticSearch


class FAQEngine:

    def __init__(self, csv_file="faq.csv"):

        self.data = pd.read_csv(csv_file)

        self.questions = self.data["question"].tolist()
        self.answers = self.data["answer"].tolist()

        self.search_engine = SemanticSearch(self.questions)

    def search(self, user_question, threshold=0.65):

        index, score = self.search_engine.search(user_question)

        if score >= threshold:
            return {
                "found": True,
                "answer": self.answers[index],
                "score": score,
                "source": "FAQ"
            }

        return {
            "found": False,
            "score": score,
            "source": "None"
        }