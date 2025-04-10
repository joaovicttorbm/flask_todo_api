from app.database import tasks_collection
from bson import ObjectId

def insert_task(task_data: dict):
    return tasks_collection.insert_one(task_data)

def find_tasks_by_user(user_id: str):
    return tasks_collection.find({"owner_id": user_id}).sort("created_at", -1)

def find_task_by_id(task_id: str):
    return tasks_collection.find_one({"_id": ObjectId(task_id)})

def update_task(task_id: str, update_data: dict):
    return tasks_collection.update_one({"_id": ObjectId(task_id)}, {"$set": update_data})

def delete_task(task_id: str):
    return tasks_collection.delete_one({"_id": ObjectId(task_id)})