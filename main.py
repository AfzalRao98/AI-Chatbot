import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# 🔐 Set your Groq API key
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

# 🤖 Initialize Groq LLM (e.g., Mixtral model)
groq_api_key=api_key,
llm = ChatGroq(model_name="meta-llama/llama-4-scout-17b-16e-instruct",)

# 🧾 Define Prompt Template
prompt = PromptTemplate(
    input_variables=["question"],
    template="""
You are a helpful and knowledgeable assistant. Answer the following user question clearly and accurately:

Question: {question}

Answer:
"""
)

# 💬 Streamlit UI
st.title("🤖 Ask Me Anything - Powered by Groq LLM")

# 📝 Text input for user question
user_question = st.text_area("Ask your question:")

# ▶️ Button to trigger LLM
if st.button("Get Answer"):
    if user_question.strip():
        with st.spinner("Thinking..."):
            # Fill the prompt with user question
            final_prompt = prompt.format(question=user_question)

            # Get response from LLM
            response = llm.invoke(final_prompt)

            # Show answer
            st.success("Here's the answer:")
            st.write(response.content)
    else:
        st.warning("Please enter a question before clicking the button.")
