from pydantic import BaseModel


class ScheduleModel(BaseModel):
    time: int