# app/settings.py
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    openai_api_key: str
    fastapi_host: str = "0.0.0.0"
    fastapi_port: int = 8000
    streamlit_port: int = 8503

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()  # type: ignore
