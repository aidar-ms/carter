import os
import re
from dotenv import load_dotenv

if os.environ.get("ENVIRONMENT") == "dev":
    load_dotenv()

# Substitution of "postgres" to "postgresql" is needed because SQLAlchemy is not happy with "postgres://"
DATABASE_URL = re.sub(r"postgres\b", "postgresql", os.environ.get("DATABASE_URL"))
REDIS_URL = os.environ.get("REDIS_URL")
