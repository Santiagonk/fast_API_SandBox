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


app = FastAPI()

@app.get('/ruta1')
def ruta1():
    return {"message": "Bienvenido a tu primera api"}

@app.post('/ruta2')
def ruta2(user: User):
    print(user)
    print(user.dict())
    return True

# Other way to run the server
if __name__ == "__main__":
    uvicorn.run("main.app", port = 8000, reload=True)