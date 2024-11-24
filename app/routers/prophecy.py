from typing import Annotated

from fastapi import APIRouter, Depends, Response, status

from app.models.prophecy import ProphecyBase, Prophecy
from app.crud.prophecy import get_prophecy, post_prophecy, delete_prophecy, \
    update_prophecy
from app.dependencies.sql_session import get_session, Session
from fastapi.security import HTTPBasic, HTTPBasicCredentials

router = APIRouter()

security = HTTPBasic()


@router.get("/api/prophecy", response_model=ProphecyBase | dict)
async def get(session: Annotated[Session, Depends(get_session)],
              credentials: Annotated[HTTPBasicCredentials, Depends(security)],
              response: Response):
    if credentials.username != "admin" or credentials.password != "admin":
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "Unauthorized"}
    return get_prophecy(session=session, response=response)


@router.post("/api/prophecy")
async def post(session: Annotated[Session, Depends(get_session)],
               credentials: Annotated[HTTPBasicCredentials, Depends(security)],
               prophecy: Prophecy, response: Response):
    if credentials.username != "admin" or credentials.password != "admin":
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "Unauthorized"}
    return post_prophecy(session=session, prophecy=prophecy, response=response)


@router.patch("/api/prophecy", response_model=ProphecyBase | dict)
async def update(session: Annotated[Session, Depends(get_session)], id: int,
                 prophecy: ProphecyBase, response: Response,
                 credentials: Annotated[HTTPBasicCredentials, Depends(security)],
                 ):
    if credentials.username != "admin" or credentials.password != "admin":
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "Unauthorized"}
    return update_prophecy(session=session, id=id, prophecy=prophecy,
                           response=response)


@router.delete("/api/prophecy", response_model=ProphecyBase | dict)
async def delete(session: Annotated[Session, Depends(get_session)], id: int,
                 response: Response, 
                 credentials: Annotated[HTTPBasicCredentials, Depends(security)],
                 ):
    if credentials.username != "admin" or credentials.password != "admin":
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "Unauthorized"}
    return delete_prophecy(session=session, id=id, response=response)
