import streamlit as st
from chatbot import get_response

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="PyMentor AI",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

.stChatMessage{
    border-radius:15px;
    padding:10px;
}

div[data-testid="stSidebar"]{
    background:#f8f9fa;
}

footer{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)


# ----------------------------
# Session State
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "faq_count" not in st.session_state:
    st.session_state.faq_count = 0

if "ai_count" not in st.session_state:
    st.session_state.ai_count = 0

# ----------------------------
# Title
# ----------------------------
st.markdown("""
# 🤖 PyMentor AI

### Your Intelligent Python Learning Assistant

Ask anything about Python.

📚 Semantic FAQ Search

🧠 Groq AI

⚡ Fast • Accurate • AI Powered
""")

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:

    st.header("📘 About")

    st.write("""
**PyMentor AI** is an intelligent Python chatbot powered by:

- 🧠 Sentence Transformers
- 🤖 Groq LLM
- 📚 Semantic FAQ Search
- 🌐 Streamlit
""")

    st.divider()

    st.subheader("📊 Chat Statistics")

    st.write(f"💬 Total Messages: {len(st.session_state.messages)}")
    st.write(f"📚 FAQ Answers: {st.session_state.faq_count}")
    st.write(f"🧠 AI Answers: {st.session_state.ai_count}")

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.session_state.faq_count = 0
        st.session_state.ai_count = 0
        st.rerun()

    st.divider()

    # Download Chat
    if st.session_state.messages:

        chat_history = ""

        for msg in st.session_state.messages:
            role = "You" if msg["role"] == "user" else "Assistant"
            chat_history += f"{role}: {msg['content']}\n\n"

        st.download_button(
            label="📥 Download Chat",
            data=chat_history,
            file_name="chat_history.txt",
            mime="text/plain"
        )

if len(st.session_state.messages) == 0:

    st.info("""
    👋 Welcome!

    I'm **PyMentor AI**.

    I can answer Python questions using:

    📚 My FAQ Knowledge Base

    🧠 Groq AI

    Try asking about python

    
    """)
    
# ----------------------------
# Display Chat History
# ----------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------
# User Input
# ----------------------------
prompt = st.chat_input("Ask me any Python question...")

if prompt:

    # Show User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant Response
    with st.chat_message("assistant"):

        with st.spinner("🤖 Thinking..."):

            result = get_response(
            prompt,
            st.session_state.messages
        )

        st.markdown(result["answer"])

        if result["source"] == "FAQ Database":

            st.success("📚 Source: FAQ Database")
            st.info(
                f"🎯 Confidence: {result['confidence']:.2f}"
            )

            st.session_state.faq_count += 1

        else:

            st.warning("🧠 Source: Groq AI")

            st.session_state.ai_count += 1

    # Save Assistant Response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result["answer"]
        }
    )

# ----------------------------
# Footer
# ----------------------------
st.divider()

st.caption("❤️ Built with Python • Streamlit • Sentence Transformers • Groq AI")