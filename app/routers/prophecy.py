from typing import Annotated

from fastapi import APIRouter, Depends, Response

from app.models.prophecy import ProphecyBase, Prophecy
from app.crud.prophecy import get_prophecy, post_prophecy, delete_prophecy, \
    update_prophecy
from app.dependencies.sql_session import get_session, Session

router = APIRouter()


@router.get("/api/prophecy", response_model=ProphecyBase | dict)
async def get(session: Annotated[Session, Depends(get_session)],
              response: Response):
    return get_prophecy(session=session, response=response)


@router.post("/api/prophecy")
async def post(session: Annotated[Session, Depends(get_session)],
               prophecy: Prophecy):
    return post_prophecy(session=session, prophecy=prophecy)


@router.patch("/api/prophecy", response_model=ProphecyBase | dict)
async def update(session: Annotated[Session, Depends(get_session)], id: int,
                 prophecy: ProphecyBase, response: Response):
    return update_prophecy(session=session, id=id, prophecy=prophecy,
                           response=response)


@router.delete("/api/prophecy", response_model=ProphecyBase | dict)
async def delete(session: Annotated[Session, Depends(get_session)], id: int,
                 response: Response):
    return delete_prophecy(session=session, id=id, response=response)
