# 🤖 PyMentor AI – Intelligent Python Learning Assistant

An AI-powered Python FAQ Chatbot developed as part of the **CodeAlpha AI Internship**.

PyMentor AI combines **Semantic Search** with **Large Language Models (Groq AI)** to answer Python programming questions accurately. It first searches a curated FAQ database using Sentence Transformers. If no suitable answer is found, it intelligently switches to Groq AI to generate a response.

---

## 🚀 Features

* 📚 Semantic FAQ Search using Sentence Transformers
* 🤖 Groq AI integration for unanswered questions
* 💬 Modern Chat Interface built with Streamlit
* 🎯 Confidence Score for FAQ matches
* 📖 Source Detection (FAQ Database / Groq AI)
* 🧠 Intelligent fallback mechanism
* 📝 Download Chat History
* 🗑️ Clear Chat functionality
* ⚡ Fast and responsive interface

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Sentence Transformers
* Scikit-learn
* Pandas
* Groq API
* python-dotenv

---

## 📂 Project Structure

```
CodeAlpha_FAQChatbot/
│
├── app.py
├── chatbot.py
├── faq_engine.py
├── embeddings.py
├── ai.py
├── faq.csv
├── requirements.txt
├── README.md
├── .env.example
│
├── assets/
└── screenshots/
```

live demo:https://codealpha-faqchatbot.streamlit.app/
---
📌 About

AI Python FAQ Chatbot is an intelligent Python learning assistant that combines Semantic Search and Groq AI to answer Python programming questions accurately. It first retrieves relevant answers from a curated FAQ database using Sentence Transformers and automatically switches to Groq AI for advanced or unseen questions, providing a fast, reliable, and interactive learning experience.
---

## 🧪 How It Works

1. User asks a Python question.
2. Sentence Transformer converts the question into an embedding.
3. Semantic similarity search finds the closest FAQ.
4. If confidence is high, the FAQ answer is returned.
5. Otherwise, Groq AI generates a detailed response.

---
Acknowledgement

This project was developed as part of the CodeAlpha Artificial Intelligence Internship Program to demonstrate practical skills in Artificial Intelligence, Natural Language Processing, Semantic Search, Large Language Model integration, API development, and interactive AI application development using Python, Streamlit, Sentence Transformers, and Groq AI.

---

## 🚀 Future Improvements

* Voice Input
* Multi-language Support
* User Authentication
* Chat History Database
* Code Execution Support
* PDF Knowledge Base

---

## 👩‍💻 Developed By

**Sriharini Guntupalli**

CodeAlpha AI Internship Project
