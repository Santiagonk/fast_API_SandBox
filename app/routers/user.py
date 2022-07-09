from fastapi import APIRouter
from app.schemas import User, UserId

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

users = []

@router.get('/')
def get_users():
    return users

@router.post('/')
def ruta2(user: User):
    print(user.dict())
    users.append(user.dict())
    return {"response": "User created succesfully"}

@router.get('/{user_id}')
def get_user_by_id(user_id: int):
    for user in users:
        print(user, type)
        if user['id'] == user_id:
            return user
    return {"message": "User Not Found"}

@router.post('/')
def obtener_usuario2(user_id:UserId):
    for user in users:
        print(user, type)
        if user['id'] == user_id.id:
            return user
    return {"message": "User Not Found"}

@router.delete('/{user_id}')
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user['id'] == user_id:
            users.pop(index)
            return {"message": "User deleted succesfully"}
    return {"message": "User Not Found"}

@router.put('/{user_id}')
def update_user(user_id: int, updateUser: User):
    for index, user in enumerate(users):
        if user['id'] == user_id:
            users[index]["first_name"] = updateUser.first_name
            users[index]["last_name"] = updateUser.last_name
            users[index]["address"] = updateUser.address
            users[index]["phone_number"] = updateUser.phone_number
            return {"message": "User updated succesfully"}
    return {"message": "User Not Found"}