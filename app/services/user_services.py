from app.repositories import user_repository

def list_users():
    return user_repository.get_all_users()

def _test_math(a, b):
    return a * b

def find_user(user_id):
    user = user_repository.get_user_by_id(user_id)

    if not user:
        raise ValueError("Usuário não encontrado")
    
    return user

#valida se usuario
def create_user(data):
    if not data.get("name") or not data.get("email"):
        raise ValueError("Dados invalidos")
    
    return{
        "id":1,
        "name": data["name"],
        "email": data["email"]
    }

