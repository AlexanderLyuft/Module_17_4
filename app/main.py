from fastapi import FastAPI
from app.routers import task, user
from app.backend.db import engine, Base
from app.models import User, Task
from sqlalchemy.schema import CreateTable

app = FastAPI()

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)

# Печать SQL для таблиц
print(CreateTable(User.__table__))
print(CreateTable(Task.__table__))


# Запуск приложения с помощью Uvicorn:
# uvicorn app.main:app --reload

