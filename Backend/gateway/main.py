from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.init import *

app = FastAPI()
origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(AuthenticationRouter)

@app.get("/")
def home():
    return "Started FastAPI on 15.4.2026...."

@app.get("/klu")
def klu1():
    return "Welcome to Y26 S4 class on 15.4.2026...."