from flask import Blueprint, request, jsonify
from app.models.task_model import Task
from app.services.task_service import (
    create_task_service, get_tasks_service,
    get_task_service, update_task_service,
    delete_task_service
)
from app.utils.error_formatter import format_validation_error
from app.utils.jwt_utils import decode_access_token
from app.utils.validators import validate_object_id
from app.utils.serializers import serialize_task
from bson.errors import InvalidId
from pydantic import ValidationError

routes = Blueprint("tasks", __name__)

def get_current_user():
    """Middleware para autenticação do usuário."""
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return None
    token = auth_header.split(" ")[1]
    payload = decode_access_token(token)
    return payload.get("sub") if payload else None

@routes.route("/tasks", methods=["POST"])
def create_task():
    """
    Insere uma nova tarefa no banco de dados.

    Args:
        task_data (dict): Dados da tarefa a ser inserida.

    Returns:
        InsertOneResult: Resultado da operação de inserção.
    """
    user_id = get_current_user()
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    try:
        task_data = Task(**request.json, owner_id=user_id)
        result = create_task_service(task_data.model_dump())
        return jsonify({"id": str(result.inserted_id)}), 201
    except ValidationError as e:
        return jsonify(format_validation_error(e)), 400

@routes.route("/tasks", methods=["GET"])
def get_tasks():
    """
    Busca todas as tarefas de um usuário específico.

    Args:
        user_id (str): ID do usuário.

    Returns:
        Cursor: Cursor com as tarefas encontradas.
    """
    user_id = get_current_user()
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    tasks = [serialize_task(t) for t in get_tasks_service(user_id)]
    return jsonify(tasks), 200

@routes.route("/tasks/<task_id>", methods=["GET"])
def get_task(task_id):
    """
    Busca uma tarefa específica pelo seu ID.

    Args:
        task_id (str): ID da tarefa.

    Returns:
        dict: Dados da tarefa encontrada ou None se não existir.
    """
    user_id = get_current_user()
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    try:
        task_id = validate_object_id(task_id)
        task = get_task_service(task_id)
        if not task or str(task["owner_id"]) != user_id:
            return jsonify({"error": "Task not found"}), 404
        return jsonify(serialize_task(task)), 200
    except InvalidId:
        return jsonify({"error": "Invalid task ID format"}), 400

@routes.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    """
    Atualiza os dados de uma tarefa específica.

    Args:
        task_id (str): ID da tarefa.
        update_data (dict): Dados a serem atualizados.

    Returns:
        UpdateResult: Resultado da operação de atualização.
    """
    user_id = get_current_user()
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    try:
        task_id = validate_object_id(task_id)
        task = get_task_service(task_id)

        if not task or str(task["owner_id"]) != user_id:
            return jsonify({"error": "Unauthorized"}), 403

        # Atualiza apenas os campos enviados no corpo da requisição
        update_data = request.json
        if not update_data:
            return jsonify({"error": "No data provided for update"}), 400

        update_task_service(task_id, update_data)
        return jsonify({"message": "Task updated"}), 200
    except InvalidId:
        return jsonify({"error": "Invalid task ID format"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    """
    Deleta uma tarefa específica pelo seu ID.

    Args:
        task_id (str): ID da tarefa.

    Returns:
        DeleteResult: Resultado da operação de exclusão.
    """
    user_id = get_current_user()
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    try:
        task_id = validate_object_id(task_id)
        task = get_task_service(task_id)
        if not task or str(task["owner_id"]) != user_id:
            return jsonify({"error": "Unauthorized"}), 403

        delete_task_service(task_id)
        return jsonify({"message": "Task deleted"}), 200
    except InvalidId:
        return jsonify({"error": "Invalid task ID format"}), 400
