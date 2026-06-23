from faq_engine import FAQEngine

faq = FAQEngine()

while True:

    question = input("Ask: ")

    result = faq.search(question)

    print(result)
    print("-" * 50)