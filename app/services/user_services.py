from app.repositories import user_repository

def list_users():
    return user_repository.get_all_users()

def find_user(user_id):
    user = user_repository.get_user_by_id(user_id)

    if not user:
        raise ValueError("Usuário não encontrado")
    
    return user

def create_user(data):
    if "name" not in data:
        raise ValueError("Nome é obrigatório")
    
    user = {
        "id": len(user_repository.get_all_users()) + 1,
        "name": data["name"]
    }
    return user_repository.create_user(user)
