from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routers import schedule, todolist
from app.database import create_tables


app = FastAPI()
app.include_router(schedule.router)
app.include_router(todolist.router)


origins = [
    "http://localhost:3000",
    "http://pomodolist.com",
    "https://pomodolist.com",
    "http://www.pomodolist.com",
    "https://www.pomodolist.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


create_tables()


@app.get("/")
def read_root():
    return {"Hello": "POMODOLIST BACKEND"}