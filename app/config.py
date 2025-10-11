# app/config.py
from dotenv import load_dotenv
import os
from pathlib import Path

# load .env from project root reliably
env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(env_path)

SECRET_KEY = os.getenv("SECRET_KEY") or os.getenv("JWT_SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY (or JWT_SECRET_KEY) not set in .env")

ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
DATABASE_URL = os.getenv("DATABASE_URL")
