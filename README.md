GenAI Agent: Перекладач + Граматичний аналізатор

Цей проєкт реалізує мовного агента з використанням LLM, який:
- Перекладає українське речення на англійську
- Пояснює використану граматику
- Переформульовує речення у більш формальному стилі

### Архітектура
- **LLM**: OpenRouter (через OpenAI API сумісний інтерфейс)
- **Backend**: FastAPI
- **UI**: Streamlit
- **Docker**: окремі контейнери для API та UI

---

## Кастомні Tools

| Tool              |                      Опис                         |
|-------------------|---------------------------------------------------|
| `explain_grammar` | Пояснює граматичну структуру англійського речення |
| `improve_style`   | Переписує речення у формальнішій, ввічливій формі |

Ці tools використовують LLM, але є кастомними, бо вони реалізовані як окремі модулі з власною логікою, prompt-інженерією та інтерфейсом.

---

## Запуск

### 1. Клонувати репозиторій ```bash git clone https://github.com/ТВОЄ_ІМ_Я/genai-language-agent.git 
cd genai-language-agent 

### 3. Створи файл .env у корені й встав свій OpenRouter API ключ: 
OPENAI_API_KEY=sk-or-...(свій ключ) 
OPENAI_API_BASE=https://openrouter.ai/api/v1 
FASTAPI_HOST=0.0.0.0 
FASTAPI_PORT=8000 
STREAMLIT_PORT=8501 

### 3. Запуск у Docker 
docker compose up --build

Після запуску:
UI: http://localhost:8501 (Streamlit)
API: http://localhost:8000/docs (FastAPI)

