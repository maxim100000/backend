import pytest

from fastapi.testclient import TestClient
from sqlmodel import Session

from sqlmodel import SQLModel, create_engine
from app.main import app


@pytest.fixture()
def create_test_database():
    from app.models.prophecy import Prophecy
    engine = create_engine("sqlite:///database.db")
    SQLModel.metadata.create_all(engine)
    return engine


@pytest.fixture()
def get_test_session_engine(create_test_database):
    def get_test_session():
        with Session(create_test_database) as session:
            yield session
    return get_test_session


@pytest.fixture(autouse=True)
def client():
    test_client = TestClient(app)
    return test_client


# @pytest.fixture(autouse=True, scope="module")
# def test_session():
#     app.dependency_overrides[get_session] = get_test_session
#     yield 
#     app.dependency_overrides = {}