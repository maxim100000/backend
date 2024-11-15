from typing import Annotated

from fastapi import APIRouter, Depends

from app.crud.prophecy import get_prophecy
from app.dependencies.sql_session import get_session, Session

router = APIRouter()

@router.get("/api/prophecy")
async def get(session: Annotated[Session, Depends(get_session)]):
    return get_prophecy(session=session)