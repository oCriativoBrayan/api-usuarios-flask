def success_response(data=None, message="Sucesso", status=200):
    return{
        "success":True,
        "message":message,
        "data":data
    }, status

def error_response(message="Erro", status=400):
    return{
        "success":False,
        "error": message
    }, status