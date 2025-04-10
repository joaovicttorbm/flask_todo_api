from app.database import users_collection

def find_user_by_email(email: str):
    user = users_collection.find_one({"email": email})
    return user

def insert_user(user_data: dict):
    user = users_collection.insert_one(user_data)
    return user