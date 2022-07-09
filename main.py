# Python
from typing import Optional
from datetime import datetime

# uvicorn
import uvicorn

# pydantic
from pydantic import BaseModel

# Fast API
from fastapi import FastAPI 

# User Model
class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    address: Optional[str]
    phone_number: int
    created_at: datetime = datetime.now()

class UserId(BaseModel):
    id:int

users = []
app = FastAPI()

@app.get('/ruta1')
def ruta1():
    return {"message": "Bienvenido a tu primera api"}

@app.get('/user')
def get_users():
    return users

@app.post('/ruta2')
def ruta2(user: User):
    print(user.dict())
    users.append(user.dict())
    return {"response": "User created succesfully"}

@app.get('/user/{user_id}')
def get_user_by_id(user_id: int):
    for user in users:
        print(user, type)
        if user['id'] == user_id:
            return user
    return {"message": "User Not Found"}

@app.post('/user')
def obtener_usuario2(user_id:UserId):
    for user in users:
        print(user, type)
        if user['id'] == user_id.id:
            return user
    return {"message": "User Not Found"}

@app.delete('/user/{user_id}')
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user['id'] == user_id:
            users.pop(index)
            return {"message": "User deleted succesfully"}
    return {"message": "User Not Found"}

@app.put('/user/{user_id}')
def update_user(user_id: int, updateUser: User):
    for index, user in enumerate(users):
        if user['id'] == user_id:
            users[index]["first_name"] = updateUser.first_name
            users[index]["last_name"] = updateUser.last_name
            users[index]["address"] = updateUser.address
            users[index]["phone_number"] = updateUser.phone_number
            return {"message": "User updated succesfully"}
    return {"message": "User Not Found"}


# Other way to run the server
if __name__ == "__main__":
    uvicorn.run("main.app", port = 8000, reload=True)