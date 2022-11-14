from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from .routers.api.routes import api_router

app = FastAPI()

origins = ['*'];

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)
origins = [
    "*",
]

app.mount("/files", StaticFiles(directory="./app/files/" , html = True), name="site")

app.include_router(api_router)



