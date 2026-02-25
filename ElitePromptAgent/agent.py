import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Initialize Groq model
llm = ChatGroq(
    model_name=os.getenv("GROQ_MODEL"),
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# Create prompt template
template = """
You are an Elite Prompt Engineering Agent.

Transform vague user input into a clean,
professional AI-ready prompt.

Rules:
- Only return final optimized prompt.
- No explanation.

User Input:
{user_input}
"""

prompt = PromptTemplate.from_template(template)

# Modern LangChain pipeline
chain = prompt | llm

def optimize_prompt(user_input: str) -> str:
    response = chain.invoke({"user_input": user_input})
    return response.content