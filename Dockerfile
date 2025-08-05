FROM python:3.11-slim

WORKDIR /app

# Встановлюємо залежності
COPY app/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо всю app/ як підмодуль
COPY app/ ./app

# Відкриваємо порт
EXPOSE 8000

# 👇 запускаємо FastAPI з правильним модулем app.main
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
