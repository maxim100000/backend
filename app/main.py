from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.prophecy import router

app = FastAPI()

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PATCH", "OPTIONS"],
    allow_headers=["*"],
)


