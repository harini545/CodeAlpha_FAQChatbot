from faq_engine import FAQEngine
from ai import ask_groq

faq = FAQEngine()


def get_response(question, history=None):
    """
    Returns a dictionary:
    {
        "answer": "...",
        "source": "FAQ" or "Groq AI",
        "confidence": float or None
    }
    """

    result = faq.search(question)

    if result["found"]:
        return {
            "answer": result["answer"],
            "source": "FAQ Database",
            "confidence": result["score"]
        }

    ai_answer = ask_groq(question, history)

    return {
        "answer": ai_answer,
        "source": "Groq AI",
        "confidence": None
    }