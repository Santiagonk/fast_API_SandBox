
# uvicorn
import uvicorn

# Fast API
from fastapi import FastAPI 

# routers
from app.routers import user

app = FastAPI()
app.include_router(user.router)

# Other way to run the server
if __name__ == "__main__":
    uvicorn.run("main.app", port = 8000, reload=True)