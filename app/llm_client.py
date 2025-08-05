# app/llm_client.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="gpt-3.5-turbo",  # або "gpt-4o" / OpenRouter модель
    temperature=0.3,
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY")
)
