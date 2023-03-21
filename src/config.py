# Packages
import os
from databases import DatabaseURL

# Mongodb
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_USER = os.getenv("MONGO_USER", "userdb")
MONGO_PASS = os.getenv("MONGO_PASSWORD", "secret-password")
MONGO_DB = os.getenv("MONGO_DB", "test")
MONGO_MAX_CONNECTIONS_COUNT = int(os.getenv("MONGO_MAX_CONNECTIONS_COUNT", 10))
MONGO_MIN_CONNECTIONS_COUNT = int(os.getenv("MONGO_MIN_CONNECTIONS_COUNT", 10))

MONGODB_URL = DatabaseURL(
    f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
)

# Redis
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "secret-password")
