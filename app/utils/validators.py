from bson import ObjectId
from flask import abort

def validate_object_id(task_id: str) -> ObjectId:
    try:
        return ObjectId(task_id)
    except Exception:
        abort(400, description=f"'{task_id}' is not a valid ObjectId.")