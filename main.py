# uvicorn
import uvicorn

# Fast API
from fastapi import FastAPI 


app = FastAPI()

@app.get('/ruta1')
def ruta1():
    return {"message": "Bienvenido a tu primera api"}

# Other way to run the server
if __name__ == "__main__":
    uvicorn.run("main.app", port = 8000)