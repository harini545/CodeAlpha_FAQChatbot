import os
from dotenv import load_dotenv
from groq import Groq

# Load .env
load_dotenv()

# Create Groq Client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_groq(question, history=None):
    """
    Ask Groq AI with optional conversation history.
    """

    messages = [
        {
            "role": "system",
            "content": """
You are PyMentor AI, an expert Python programming tutor.

Rules:
- Answer ONLY Python programming related questions.
- If the question is unrelated to Python, politely explain that you only answer Python-related questions.
- Explain concepts in a beginner-friendly way.
- Give examples whenever useful.
- Keep answers concise unless the user asks for more details.
- Use Markdown formatting.
"""
        }
    ]

    # Add recent conversation history (last 6 messages)
    if history:
        for msg in history[-6:]:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

    # Current user question
    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.3,
            max_tokens=600
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error: {e}"