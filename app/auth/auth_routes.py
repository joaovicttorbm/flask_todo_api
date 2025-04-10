from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from app.models.user_model import User, UserLogin
from app.services.user_service import register_user, login_user
from app.utils.error_formatter import format_validation_error

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():
    """
    Endpoint para registrar um novo usuário.

    Recebe os dados do usuário no corpo da requisição (JSON),
    valida os dados usando Pydantic e registra o usuário no banco de dados.

    Retorna:
        - 201: Mensagem de sucesso se o registro for concluído.
        - 400: Mensagem de erro se os dados forem inválidos ou o e-mail já estiver registrado.
    """
    try:
        user_data = User(**request.json)  # Valida os dados com Pydantic
        result = register_user(user_data.model_dump())  
        if not result:
            return jsonify({"error": "User registration failed"}), 400
        return jsonify({"message": "User registered successfully"}), 201
    except ValidationError as e:
        return jsonify(format_validation_error(e)), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400  

@auth.route("login", methods=["POST"])
def login(): 
    """
    Endpoint para autenticar um usuário.

    Recebe os dados de login no corpo da requisição (JSON),
    valida os dados usando Pydantic e verifica as credenciais do usuário.

    Retorna:
        - 200: Mensagem de sucesso e token JWT se as credenciais forem válidas.
        - 400: Mensagem de erro se os dados forem inválidos ou as credenciais estiverem incorretas.
    """
    try:
        login_data = UserLogin(**request.json)
        token = login_user(login_data.email, login_data.password)
        return jsonify({"message": "Login successful", "token": token}), 200
    except ValidationError as e:
        return jsonify(format_validation_error(e)), 400