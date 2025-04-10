from bson import ObjectId

def serialize_task(task):
    task["_id"] = str(task["_id"])
    return task

def serialize_user(user):
    user["_id"] = str(user["_id"])
    return user