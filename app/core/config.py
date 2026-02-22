import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Meesaw Webhook Service"
    PROJECT_VERSION: str = "1.0.0"
    
    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD : str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","tdd")
    DATABASE_URL = f"sqlite:///./webhooks.db" # Keeping sqlite for now based on current app

    SHARED_SECRET: str = os.getenv("SHARED_SECRET", "supersecret")

settings = Settings()
