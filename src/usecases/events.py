# Packages
import json

import redis
from starlette import status
from typing import Dict, List
from motor.motor_asyncio import AsyncIOMotorClient

# Modules
from utils.helper import ReturnValue


class EventsUsecase:
    @staticmethod
    async def add(db: AsyncIOMotorClient, documents: List[Dict]) -> ReturnValue:
        """
        Add payload received from mandrill to database
        Args:
            db: database object
            documents: payload

        Returns:
            ReturnValue object
        """
        # Deleting existing id since its getting repeated
        for doc in documents:
            del doc["_id"]

        await db.events.insert_many(documents)
        return ReturnValue(True, status.HTTP_200_OK, "Event added to db")

    @staticmethod
    def add_to_cache(redis_db: redis.Redis, payload: List[Dict]) -> ReturnValue:
        """
        Add payload received from mandrill to cache memory
        Args:
            redis_db: redis client object
            payload: data to be inserted into cache

        Returns:
            ReturnValue object
        """
        pipe = redis_db.pipeline()

        for p in payload:
            key = p["_id"]
            name = p["event"]
            value = json.dumps(p)
            pipe.hset(key, name, value)

        pipe.execute()
        return ReturnValue(True, status.HTTP_200_OK, "Event added to cache")

    @staticmethod
    def get(redis_db: redis.Redis) -> ReturnValue:
        """
        Retrieves events data from cache
        Args:
            redis_db: redis client object

        Returns:
            ReturnValue object
        """
        keys = redis_db.keys()
        pipe = redis_db.pipeline()
        for key in keys:
            pipe.hgetall(key)

        result = pipe.execute()
        return ReturnValue(True, status.HTTP_200_OK, "Data fetched", data=result)
