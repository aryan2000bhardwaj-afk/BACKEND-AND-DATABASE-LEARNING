from fastapi import APIRouter, Header
from models.schemas import TasksSchema
import httpx

router = APIRouter(prefix="/taskservice")

SPRING_URL = "http://localhost:8002/"

@router.post("/createtask")
async def createTask(T: TasksSchema, Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            SPRING_URL + "task/createtask",
            json=T.model_dump(),
            headers = {"Token": Token}
        )
    return response.json() # Returs back the response received from spring