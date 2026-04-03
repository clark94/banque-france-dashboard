import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/banque_france_db")
MODEL_PATH = os.getenv("MODEL_PATH", "model/model.pkl")
DATA_PATH = os.getenv("DATA_PATH", "data/raw/flux-et-taux-la-ldds-lep.csv")
APP_HOST = os.getenv("APP_HOST", "127.0.0.1")
APP_PORT = int(os.getenv("APP_PORT", "8000"))
