from bson import ObjectId
from bson.errors import InvalidId

def validate_object_id(task_id: str) -> ObjectId:
    try:
        return ObjectId(task_id)
    except InvalidId:
        raise InvalidId(f"'{task_id}' is not a valid ObjectId.")