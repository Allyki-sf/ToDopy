from fastapi import FastAPI
from app.routes import auth, tasks

app = FastAPI(title="ToDO api")

app.include_router(auth.router)
app.include_router(tasks.router)