from typing import Union
from pydantic import BaseModel


class AddTodoModel(BaseModel):
    todo: str
    done: bool


class UpdateTodoModel(BaseModel):
    id: int
    todo: str
    done: bool

class DeleteTodoModel(BaseModel):
    id: int