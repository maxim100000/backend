from fastapi import Response, status
from sqlmodel import select, func

from app.models.prophecy import Prophecy, ProphecyBase
from app.dependencies.sql_session import Session
from app.utils.check_unique import check_similarity


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
    if prophecy.content == "" or len(prophecy.content) < 15 or len(
            prophecy.content) > 350:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "Bad request. Content must be between 15 and 350 symbols"}
    try:
        for item in session.exec(select(Prophecy)).fetchall():
            if check_similarity(prophecy.content, item.content):
                return {"message": "Цитата слишком похожа на одну из имеющихся"}
    except:
        pass

    prophecy = Prophecy.model_validate(prophecy)
    try:
        session.add(prophecy)
        session.commit()
    except:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Server error"}
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
    if prophecy.content == "" or len(prophecy.content) < 15 or len(
            prophecy.content) > 350:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return  {"message": "Bad request. Content must be between 15 and 350 symbols"}
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
