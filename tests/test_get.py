from fastapi import FastAPI
from fastapi.testclient import TestClient

from sqlmodel import SQLModel,create_engine, Session
from app.main import app

from app.dependencies.sql_session import get_session
from app.models.prophecy import Prophecy

client = TestClient(app)

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)


def get_test_session():
    with Session(engine) as session:
        yield session


def test_post_prophecy():
    app.dependency_overrides[get_session] = get_test_session
    
    response = client.post("/api/prophecy",
                           json={"content": "description"},
                           headers={"Authorization": "Basic YWRtaW46YWRtaW4="}
                           )
    assert response.status_code == 200
    print(response.json())
    
    app.dependency_overrides = {}


def test_get_prophecy():
    app.dependency_overrides[get_session] = get_test_session
  
    response = client.get("/api/prophecy",
                          headers={"Authorization": "Basic YWRtaW46YWRtaW4="})
    assert response.status_code == 200
    print(response.json())
  
    app.dependency_overrides = {}
    
    
def test_delete_prophecy():
    app.dependency_overrides[get_session] = get_test_session
  
    response = client.delete("/api/prophecy",
                          headers={"Authorization": "Basic YWRtaW46YWRtaW4="},
                          params={"id": 1}
                          )
    assert response.status_code == 200
    print(response.json())
  
    app.dependency_overrides = {}

    
def test_update_prophecy():
    app.dependency_overrides[get_session] = get_test_session
  
    response = client.patch("/api/prophecy",
                          headers={"Authorization": "Basic YWRtaW46YWRtaW4="},
                          json={"content": "вызов"},
                          params={"id": 1}
                          )
    assert response.status_code == 200
    print(response.json())
    
    app.dependency_overrides = {}
        



    
    
     
