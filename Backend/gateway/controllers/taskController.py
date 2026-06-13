# =======================================================================TASK CONTROLLER=====================================================
from fastapi import APIRouter,Header
from models.schemas import TaskSchema
import httpx


router = APIRouter(prefix="/taskservice")

SPRING_URL = "http://localhost:8002/"



@router.post("/createtask")
async def createtask(T: TaskSchema, token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            SPRING_URL + "task/createtask",
            json=T.model_dump(),
            headers={"Token": token}
        )
    return response.json()

@router.get("/getalltasks/{PAGE}/{SIZE}")
async def getAllTasks(PAGE: int, SIZE:int, token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            SPRING_URL + f"task/getalltasks/{PAGE}/{SIZE}",
            headers = {"Token": token}
        )
    return response.json()


@router.get("/gettask/{ID}")
async def getTask(ID: str, Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            SPRING_URL + f"task/gettask/{ID}",
            headers = {"Token": Token}
        )
    return response.json()

@router.delete("/deletetask/{ID}")
async def deleteFunction(ID: str, token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            SPRING_URL + f"task/deletetask/{ID}",
            headers = {"Token": token}
        )
    return response.json()

# ✅ FIXED: Changed from client.delete to client.put
@router.put("/updatetask/{ID}")
async def updateFunction(ID: str, T: TaskSchema, token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        response = await client.put(  # ✅ Fixed: was client.delete
            SPRING_URL + f"task/updatetask/{ID}",
            json=T.model_dump(),  # ✅ Added: Send the task data
            headers = {"Token": token}
        )
    return response.json()


@router.get("/vectorsearch/{QUERY}")
async def vectorSearch(QUERY: str, Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            SPRING_URL + f"task/vectorsearch/{QUERY}",
            headers={"Token": Token}
        )

    print("STATUS =", response.status_code)
    print("BODY =", response.text)

    return response.json()