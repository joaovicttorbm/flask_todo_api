from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from app.models.user_model import User, UserLogin
from app.services.user_service import register_user, login_user
from app.utils.error_formatter import format_validation_error

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():
    try:
        user_data = User(**request.json)  # Valida os dados com Pydantic
        result = register_user(user_data.model_dump())  # Passa como dicionário
        return jsonify({"message": "User registered successfully"}), 201
    except ValidationError as e:
        return jsonify(format_validation_error(e)), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400  # Retorna mensagem de erro apropriada

@auth.route("login", methods=["POST"])
def login():
    try:
        login_data = UserLogin(**request.json)
        token = login_user(login_data.email, login_data.password)
        return jsonify({"message": "Login successful", "token": token}), 200
    except ValidationError as e:
        return jsonify(format_validation_error(e)), 400