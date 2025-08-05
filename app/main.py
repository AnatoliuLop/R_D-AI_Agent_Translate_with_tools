# app/main.py
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.openai_agent import llm, explain_grammar, improve_style

app = FastAPI()

class QueryRequest(BaseModel):
    question: str  # Українською

@app.post("/query")
async def query_agent(request: QueryRequest):
    if not request.question:
        raise HTTPException(status_code=400, detail="Question is required")

    try:
        # 1. Переклад українського речення англійською
        translate_prompt = f"Translate the following Ukrainian sentence to English:\n\n{request.question}"
        english_msg = llm.invoke(translate_prompt)
        english = english_msg.content.strip()

        # 2. Граматичний аналіз англійського речення
        grammar = explain_grammar(english)

        # 3. Формалізація стилю (переписати англ. речення офіційно)
        styled = improve_style(english)

        return {
            "ukrainian_input": request.question,
            "translation": english,
            "grammar_explanation": grammar,
            "formal_version": styled
        }

    except Exception as e:
        logging.error(f"Agent error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
