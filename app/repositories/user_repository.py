_users = []

def get_all_users():
    return _users

def get_user_by_id(user_id):
    return next((u for u in _users if u["id"] == user_id), None)

def create_user(user):
    _users.append(user)
    return user