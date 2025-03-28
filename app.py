import streamlit as st
from retrieval import retrieve_relevant_docs
from gpt_generation import generate_answer

st.title("🔍 RAG Chatbot")

# ✅ Ask user for OpenAI API Key
api_key = st.text_input("🔑 Enter your OpenAI API Key:", type="password")

query = st.text_input("💬 Ask me anything:")

if api_key and query:
    retrieved_docs = retrieve_relevant_docs(query)

    st.subheader("📖 Retrieved Context:")
    if retrieved_docs:
        for doc in retrieved_docs:
            st.write(f"- {doc}")
    else:
        st.write("⚠️ No relevant documents found.")

    answer = generate_answer(api_key, query, retrieved_docs)
    
    st.subheader("🤖 AI Answer:")
    st.write(answer)

elif not api_key:
    st.warning("⚠️ Please enter your OpenAI API Key to proceed.")
