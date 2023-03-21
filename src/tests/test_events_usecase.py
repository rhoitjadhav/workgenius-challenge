# Packages
import asyncio
import unittest

# Packages
from db.redisdb import get_redis_db
from usecases.events import EventsUsecase
from db.mongodb import get_database, connect_to_mongo, close_mongo_connection


class TestEventsUsecase(unittest.TestCase):
    _events = EventsUsecase()
    _redis_db = get_redis_db()
    asyncio.run(connect_to_mongo())
    _mongodb = asyncio.run(get_database())

    def setUp(self) -> None:
        pass

    def test_add_payload_to_database(self):
        """
        Test functionality of add payload to mongodb database
        """
        documents = [
            {
                "event": "send",
                "msg": {
                    "ts": 1365109999,
                    "subject": "This an example webhook message",
                    "email": "example.webhook@mandrillapp.com",
                    "sender": "example.sender@mandrillapp.com",
                    "tags": ["webhook-example"],
                    "opens": [],
                    "clicks": [],
                    "state": "sent",
                    "metadata": {"user_id": 111},
                    "_version": "exampleaaaaaaaaaaaaaaa",
                    "_id": "exampleaaaaaaaaaaaaaaaaaaaaaaaaa",
                },
                "_id": "exampleaaaaaaaaaaaaaaaaaaaaaaaaa",
                "ts": 1384954004
            }
        ]
        args = [self._mongodb, documents]
        result = asyncio.run(self._events.add(*args))
        self.assertTrue(result.status)

    def test_add_payload_to_redis_cache(self):
        """
        Test functionality of add payload to redis cache memory
        """
        payload = [
            {
                "event": "send",
                "msg": {
                    "ts": 1365109999,
                    "subject": "This an example webhook message",
                    "email": "example.webhook@mandrillapp.com",
                    "sender": "example.sender@mandrillapp.com",
                    "tags": ["webhook-example"],
                    "opens": [],
                    "clicks": [],
                    "state": "sent",
                    "metadata": {"user_id": 111},
                    "_id": "exampleaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "_version": "exampleaaaaaaaaaaaaaaa"
                },
                "_id": "exampleaaaaaaaaaaaaaaaaaaaaaaaaa",
                "ts": 1384954004
            }
        ]
        result = self._events.add_to_cache(self._redis_db, payload)
        self.assertTrue(result.status)

    def test_get_events_from_redis_cache(self):
        """
        Test functionality of retrival of events cache data
        """
        result = self._events.get(self._redis_db)
        self.assertTrue(result.status)
