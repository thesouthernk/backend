from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from .routers.api.routes import api_router

app = FastAPI()

origins = ['*','https://cheery-gelato-5b9506.netlify.app/'];

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/files", StaticFiles(directory="./app/files/" , html = True), name="site")

app.include_router(api_router)



