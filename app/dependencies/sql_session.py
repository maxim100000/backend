from sqlmodel import Session

from app.utils.database_engine import engine


def get_session() -> Session:
    with Session(engine) as session:
        yield session