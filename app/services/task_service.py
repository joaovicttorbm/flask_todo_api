from app.repository.task_repository import (
    insert_task, find_tasks_by_user, find_task_by_id,
    update_task, delete_task
)

def create_task_service(task_data):
    return insert_task(task_data)

def get_tasks_service(user_id):
    return find_tasks_by_user(user_id)

def get_task_service(task_id):
    return find_task_by_id(task_id)

def update_task_service(task_id, data):
    return update_task(task_id, data)

def delete_task_service(task_id):
    return delete_task(task_id)