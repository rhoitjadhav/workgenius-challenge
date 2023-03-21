# Packages
from redis import Redis
from config import REDIS_HOST, REDIS_PORT


def get_redis_db():
    """
    Create Redis client object
    Returns:
        Redis instance
    """
    client = Redis(REDIS_HOST, REDIS_PORT, decode_responses=True)
    return client
