from starlette import status
from fastapi import Response

from app.models.prophecy import Prophecy, ProphecyBase
from app.dependencies.sql_session import Session
from sqlmodel import select, func


def get_prophecy(session: Session, response: Response):
    prophecy = session.exec(
        select(Prophecy).where(Prophecy.used == False).order_by(
            func.random())).first()
    if prophecy:
        prophecy.used = True
        session.add(prophecy)
        session.commit()
        session.refresh(prophecy)
        return prophecy
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Prophecy not found"}


def post_prophecy(session: Session, prophecy: Prophecy):
    prophecy = Prophecy.model_validate(prophecy)
    try:
        session.add(prophecy)
        session.commit()
    except Exception:
        raise Exception("Something went wrong")
    else:
        session.refresh(prophecy)
        return prophecy


def delete_prophecy(session: Session, id: int, response: Response):
    prophecy = session.get(Prophecy, id)
    if not prophecy:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Prophecy not found"}
    session.delete(prophecy)
    session.commit()
    return {"deleted": True}


def update_prophecy(session: Session, id: int, prophecy: ProphecyBase,
                    response: Response):
    db_prophecy = session.get(Prophecy, id)
    if not db_prophecy:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Prophecy not found"}
    else:
        db_prophecy.sqlmodel_update(prophecy, update={"used": True})
        session.add(db_prophecy)
        session.commit()
        session.refresh(db_prophecy)
        return db_prophecy
