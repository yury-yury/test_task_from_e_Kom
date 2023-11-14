from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient

from settings import settings

# synchronous access to the database
client = MongoClient(settings.DATABASE_URL)
db = client[settings.DB_NAME]
collection = db[settings.DB_COLLECTION]

# asynchronous access to the database
async_client = AsyncIOMotorClient(settings.DATABASE_URL)
async_db = async_client[settings.DB_NAME]
async_collection = async_db[settings.DB_COLLECTION]
