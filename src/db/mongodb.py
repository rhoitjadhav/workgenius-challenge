# Packages
from motor.motor_asyncio import AsyncIOMotorClient

# Modules
from config import MONGODB_URL, MONGO_MAX_CONNECTIONS_COUNT, MONGO_MIN_CONNECTIONS_COUNT, MONGO_DB


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_database() -> AsyncIOMotorClient:
    return db.client[MONGO_DB]


async def connect_to_mongo():
    print("Connecting to database...")
    db.client = AsyncIOMotorClient(str(MONGODB_URL),
                                   maxPoolSize=MONGO_MAX_CONNECTIONS_COUNT,
                                   minPoolSize=MONGO_MIN_CONNECTIONS_COUNT)
    print("Database connected！")


async def close_mongo_connection():
    print("Closing database connection...")
    db.client.close()
    print("Database closed！")
