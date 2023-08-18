from fastapi import FastAPI
from models import Todo
    
app = FastAPI()

@app.get('/')
async def root():
    return {"message":"Hello world"}

todos = []

# get all Todos
@app.get('/todos')
async def get_todos():
    return {"todos":todos}
    
# get single Todo
@app.get('/todos/{todo_id}')
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo":todo}
    return {"message":"no todo found!"}
    
# # create a Todo
@app.post('/todos')
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message": "Todo has been added!"}

# # update a Todo
# @app.get('/')
# async def update_todo():
    
# # delete a Todo
@app.delete('/todos/{todo_id}')
async def get_delete(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo has been removed!"}
    return {"message":"no todo found!"}