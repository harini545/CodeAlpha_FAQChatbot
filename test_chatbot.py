from chatbot import get_response

while True:
    question = input("Ask: ")

    result = get_response(question)

    print("\nAnswer:")
    print(result["answer"])

    print("\nSource:", result["source"])

    if result["confidence"] is not None:
        print("Confidence:", round(result["confidence"], 2))

    print("-" * 60)