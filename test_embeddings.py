from embeddings import SemanticSearch

questions = [
    "What is Python?",
    "What is a tuple?",
    "What is Streamlit?"
]

search = SemanticSearch(questions)

while True:
    q = input("Ask: ")

    index, score = search.search(q)

    print("\nBest Match:")
    print(questions[index])
    print("Similarity:", round(score, 3))
    print("-" * 40)