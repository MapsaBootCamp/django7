from config.db import users_collection
from models.User import User
from schema.User import user_helper
from bson.objectid import ObjectId

from utils import get_password_hash, verify_password

# Retrieve all students present in the database
async def retrieve_users():
    users = []
    async for user in users_collection.find():
        users.append(user_helper(user))
    return users

# Add a new student into to the database
async def add_user(user_data: dict) -> dict:
    user_data["password"] = get_password_hash(user_data["password"])
    user = await users_collection.insert_one(user_data)
    new_user = await users_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)

# Retrieve a student with a matching ID
async def retrieve_user(id: str) -> dict:
    user = await users_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)
    else:
        raise Exception("user not found")

# Update a student with a matching ID
async def update_user(user: User, data: dict):
    user = await users_collection.find_one({"username": user["username"]})
    if user:
        updated_user = await users_collection.update_one(
            {"username": user["username"]}, {"$set": data}
        )
        return updated_user
    else:
        raise Exception("user not found")

# Delete a student from the database
async def delete_user(id: str):
    user = await users_collection.find_one({"_id": ObjectId(id)})
    if user:
        await users_collection.delete_one({"_id": ObjectId(id)})
        return True

async def authenticate_user(username: str, password: str):
    user = await users_collection.find_one({"username": username})
    print(user)
    if not user:
        return False
    if not verify_password(password, user["password"]):
        return False
    return user















