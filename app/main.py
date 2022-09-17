from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routers import schedule
from app.database import create_tables


app = FastAPI()
app.include_router(schedule.router)


create_tables()


@app.get("/")
def read_root():
    return {"Hello": "POMODOLIST BACKEND"}