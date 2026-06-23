from ai import ask_groq

while True:
    question = input("Ask: ")

    print()
    print(ask_groq(question))
    print("-" * 50)