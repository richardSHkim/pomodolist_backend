from curses.ascii import TAB
from fastapi import APIRouter

from app.models.TodoModel import AddTodoModel, UpdateTodoModel, DeleteTodoModel
from app.database import conn


router = APIRouter(prefix='/api/todolist',
                    tags=['todolist'])


@router.get("/")
def get_todolist():
    cur = conn.cursor()
    cur.execute("SELECT * FROM todolist ORDER BY id ASC")
    todolist = [{
        'id': x[0],
        'todo': x[1],
        'done': x[2]
    } for x in cur.fetchall()]
    conn.commit()

    return {"todolist": todolist}


@router.post("/")
def add_todo(body: AddTodoModel):
    cur = conn.cursor()
    cur.execute("""INSERT INTO  todolist ( todo, done )
                    VALUES ( %s, %s )""" , [body.todo, body.done])
    conn.commit()

    todolist = get_todolist()
    return {"message": "add success", "todolist": todolist["todolist"]}


@router.put("/")
def update_todo(body: UpdateTodoModel):
    cur = conn.cursor()
    cur.execute("""UPDATE todolist SET 
                    todo = %s, done = %s WHERE id = %s""", [body.todo, body.done, body.id])
    conn.commit()

    todolist = get_todolist()
    return {"message": "update success", "todolist": todolist["todolist"]}


@router.delete("/")
def delete_todo(body: DeleteTodoModel):
    cur = conn.cursor()
    cur.execute("DELETE FROM todolist WHERE id = %s", [body.id])
    conn.commit()

    todolist = get_todolist()
    return {"message": "delete success", "todolist": todolist["todolist"]}