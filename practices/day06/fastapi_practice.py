from fastapi import FastAPI
from pydantic import BaseModel, Field


class TaskCreateRequest(BaseModel):
    title: str = Field(min_length=1)
    priority: int = Field(ge=1, le=5)
    assignee: str | None = None


class TaskInDB(BaseModel):
    id: int
    title: str
    priority: int
    internal_note: str


class TaskOut(BaseModel):
    id: int
    title: str
    priority: int


app = FastAPI()


@app.get("/square/{number}")
async def square(number: int):
    return {"result": number ** 2}


@app.get("/search")
async def search(q: str, page: int = 1, page_size: int = 10):
    return {"query": q, "page": page, "page_size": page_size}


@app.post("/tasks")
async def tasks(req: TaskCreateRequest):
    return req


@app.get("/task/1", response_model=TaskOut)
async def get_task():
    return TaskInDB(
        id=100,
        title="hello",
        priority=1,
        internal_note="wonder"
    )