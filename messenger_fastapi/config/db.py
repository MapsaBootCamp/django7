import motor.motor_asyncio
from pymongo import TEXT

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.messenger

users_collection = database.get_collection("users")

users_collection.create_index([('username', TEXT)], default_language='english')
