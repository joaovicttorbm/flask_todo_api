from app.database import users_collection

def find_user_by_email(email: str):
    user = users_collection.find_one({"email": email})
    print(f"Finding user by email: {email}, Result: {user}")
    return user

def insert_user(user_data: dict):
    user = users_collection.insert_one(user_data)
    print(f"Insert user: {user_data}, Result: {user}")
    return user