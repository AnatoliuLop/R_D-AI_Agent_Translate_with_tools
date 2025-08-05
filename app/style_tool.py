# app/style_tool.py
from app.llm_client import llm

def improve_style(sentence: str) -> str:
    prompt = f"""
    Перефразуй наступне речення у **більш офіційній формі**, зберігаючи його зміст:

    "{sentence}"

    Зроби стиль професійним і ввічливим. Виведи тільки переписане речення.
    """
    return llm.invoke(prompt).content
