
from fastapi import FastAPI, Header
from typing import Annotated

app = FastAPI()

@app.get("/")
async def root(x_head: Annotated[str, Header()]):
    return {"message": "Привет", "X-Head": x_head}