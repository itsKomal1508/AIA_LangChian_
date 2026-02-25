import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Safety check
if "GROQ_API_KEY" not in st.secrets:
    st.error("GROQ_API_KEY not found in Streamlit secrets.")
    st.stop()

if "GROQ_MODEL" not in st.secrets:
    st.error("GROQ_MODEL not found in Streamlit secrets.")
    st.stop()

llm = ChatGroq(
    model_name=st.secrets["GROQ_MODEL"],
    groq_api_key=st.secrets["GROQ_API_KEY"]
)

def optimize_prompt(user_input: str) -> str:
    prompt = ChatPromptTemplate.from_template(
        "Rewrite this messy idea into a professional AI-ready prompt:\n\n{input}"
    )

    chain = prompt | llm
    response = chain.invoke({"input": user_input})

    return response.content