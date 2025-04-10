from app.utils.password_utils import hash_password, verify_password
from app.utils.jwt_utils import create_access_token
from app.repository.user_repository import find_user_by_email, insert_user

def register_user(user_data):
    if find_user_by_email(user_data["email"]):
        raise ValueError("User already exists")

    hashed = hash_password(user_data["password"])  
    user_data["password"] = hashed  # Atualiza o dicionário com a senha hash
    insert_user(user_data)  
    return {"message": "User created successfully"}

def login_user(email: str, password: str):
    user = find_user_by_email(email)
    if not user or not verify_password(password, user["password"]):
        raise ValueError("Invalid credentials")
    token = create_access_token({"sub": str(user["_id"]), "email": user["email"]})
    return {"access_token": token}