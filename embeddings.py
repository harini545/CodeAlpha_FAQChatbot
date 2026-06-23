from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

print("Loading Sentence Transformer model... (first time may take a minute)")
model = SentenceTransformer("all-MiniLM-L6-v2")
print("✅ Model loaded successfully!")

class SemanticSearch:
    def __init__(self, questions):
        self.questions = questions
        self.embeddings = model.encode(
            questions,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

    def search(self, query):
        query_embedding = model.encode(
            query,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        similarities = cosine_similarity(
            [query_embedding],
            self.embeddings
        )[0]

        best_index = np.argmax(similarities)
        best_score = similarities[best_index]

        return best_index, float(best_score)