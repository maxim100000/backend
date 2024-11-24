from fastapi import Response, status
from sqlmodel import select, func

from app.models.prophecy import Prophecy, ProphecyBase
from app.dependencies.sql_session import Session
from app.utils.check_unique import check_similarity
from app.utils.database_utils import get_all


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
        return {"message": "New prophecy not found"}


def post_prophecy(session: Session, prophecy: Prophecy, response: Response):
    try:
        for item in get_all():
            if check_similarity(prophecy.content, item):
                return {"message":"Цитата слишком похожа на одну из имеющихся"}
    except Exception:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"message": "Сервер недоступен"}
    else:
        prophecy = Prophecy.model_validate(prophecy)
        try:
            session.add(prophecy)
            session.commit()
        except Exception:
            return {"message":"Something went wrong"}
        else:
            session.refresh(prophecy)
            return prophecy


def delete_prophecy(session: Session, id: int, response: Response):
    db_prophecy = session.get(Prophecy, id)
    if not db_prophecy:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Prophecy not found"}
    session.delete(db_prophecy)
    session.commit()
    return {"message": "deleted"}


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
        return {"message": "updated"}
