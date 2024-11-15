from app.models.prophecy import Prophecy
from app.dependencies.sql_session import Session
from app.utils.database_utils import random_from_count

def get_prophecy(session: Session): 
    return session.get(Prophecy, random_from_count())