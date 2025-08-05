# app/grammar_tool.py
from app.llm_client import llm

def explain_grammar(sentence: str) -> str:
    """
    Пояснює граматику англійського речення за допомогою LLM.
    """
    prompt = f"""
    Поясни граматичну структуру цього речення:

    "{sentence}"

    Поясни в простий спосіб, які часи або граматичні конструкції були використані.
    Виведи лише пояснення.
    """
    return llm.invoke(prompt).content
