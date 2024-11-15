from fastapi import FastAPI

from app.routers.prophecy import router

app = FastAPI()
app.include_router(router)

