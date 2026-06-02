import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

print("API Key Found:", os.getenv("GROQ_API_KEY") is not None)

llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

response = llm.invoke("Say hello")

print(response.content)