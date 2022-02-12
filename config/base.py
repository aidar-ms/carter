import os
from dotenv import load_dotenv

if os.environ.get("ENVIRONMENT") == "dev":
    load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")
REDIS_URL = os.environ.get("REDIS_URL")
