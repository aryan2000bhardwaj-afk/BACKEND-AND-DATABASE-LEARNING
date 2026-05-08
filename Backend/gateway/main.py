from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.authenticationController import router as AuthenticationRouter
app = FastAPI()
origins = ["http://localhost:5713"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(AuthenticationRouter)
@app.get("/")
def home():
    return "Started FastAPI on port 8000"

@app.get("/klu")
def klu1():
    return "Welcome to KLU"