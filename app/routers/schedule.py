from fastapi import APIRouter

from app.models.ScheduleModel import ScheduleModel
from app.database import conn


router = APIRouter(prefix='/api/schedule',
                    tags=['schedule'])


@router.get("/")
def get_scedule():
    cur = conn.cursor()
    cur.execute("SELECT time FROM schedules")
    schedule = [x[0] for x in cur.fetchall()]
    conn.commit()

    return {"schedule": schedule}


@router.post("/")
def add_schedule(body: ScheduleModel):
    cur = conn.cursor()
    cur.execute("INSERT INTO schedules (time) VALUES (%s)", [body.time])
    conn.commit()

    return {"message": "success"}


@router.delete("/")
def clear_schedule():
    cur = conn.cursor()
    cur.execute("TRUNCATE TABLE schedules")
    conn.commit()

    return {"message": "success"}