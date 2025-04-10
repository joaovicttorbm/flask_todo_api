from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI_DEV", "mongodb://localhost:27017/todo_db")

client = MongoClient(MONGO_URI)
print("Connected to MongoDB...")
db = client.get_database()
users_collection = db["users"]
tasks_collection = db["tasks"]
