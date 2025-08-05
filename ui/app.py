# app.py
import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.title("🎓 Language Assistant Agent")

ukr_prompt = st.text_input("Введіть українське речення для перекладу та аналізу:")

if st.button("Аналізувати") and ukr_prompt:
    response = requests.post(f"{API_URL}/query", json={"question": ukr_prompt})
    if response.status_code == 200:
        result = response.json()
        st.success(f"📤 Переклад:\n{result['translation']}")
        st.info(f"📘 Пояснення граматики:\n{result['grammar_explanation']}")
        st.warning(f"🪄 Формальна версія:\n{result['formal_version']}")
    else:
        st.error(f"❌ Помилка: {response.text}")
