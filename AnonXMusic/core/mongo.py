from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("Connecting to your Mongo Database...")
try:
    _mongo_async_ = AsyncIOMotorClient(mongodb+srv://Devil:8dTwwn8LFba8dyj@cluster0.7frtspj.mongodb.net/?retryWrites=true&w=majority)
    mongodb = _mongo_async_.Devil
    LOGGER(__name__).info("Connected to your Mongo Database.")
except:
    LOGGER(__name__).error("Failed to connect to your Mongo Database.")
    exit()
