from sqlmodel import create_engine, SQLModel

from app.dependencies.sql_session import get_session, Session
from app.main import app


def test_get_status_backend(client):

    response = client.get("/api/health",
                          headers={"Authorization": "Basic YWRtaW46YWRtaW4="})
    assert response.status_code == 200
    print(response.json())


def test_get_prophecy(client, get_test_session_engine):
    app.dependency_overrides[get_session] = get_test_session_engine

    response = client.get("/api/prophecy",
                          headers={"Authorization": "Basic YWRtaW46YWRtaW4="})
    print(response.json())
    assert response.status_code == 200

    app.dependency_overrides = {}
    

def test_get_all_prophecy(client, get_test_session_engine):
    app.dependency_overrides[get_session] = get_test_session_engine

    response = client.get("/api/prophecy/all",
                          headers={"Authorization": "Basic YWRtaW46YWRtaW4="})
    assert response.status_code == 200
    print(response.json())

    app.dependency_overrides = {}


def test_post_prophecy(client, get_test_session_engine):
    app.dependency_overrides[get_session] = get_test_session_engine

    response = client.post("/api/prophecy",
                           json={"content": "".join(['a' for _ in range(15)])},
                           headers={"Authorization": "Basic YWRtaW46YWRtaW4="}
                           )
    print(response.json())
    assert response.status_code == 200

    app.dependency_overrides = {}


def test_put_prophecy(client, get_test_session_engine):
    app.dependency_overrides[get_session] = get_test_session_engine

    response = client.put("/api/prophecy/1",
                            json={"content": "будь смелым, как два бобра"},
                            headers={"Authorization": "Basic YWRtaW46YWRtaW4=", 
                                     "Content-Type": "application/json"
                                     }
                            )
    print(response.json())
    assert response.status_code == 200

    app.dependency_overrides = {}


def test_patch_status(client, get_test_session_engine):
    app.dependency_overrides[get_session] = get_test_session_engine

    response = client.patch("/api/prophecy/1",
                            headers={"Authorization": "Basic YWRtaW46YWRtaW4="}
                            )
    print(response.json())
    assert response.status_code == 200

    app.dependency_overrides = {}


def test_delete_prophecy(client, get_test_session_engine):
    app.dependency_overrides[get_session] = get_test_session_engine

    response = client.delete("/api/prophecy/1",
                             headers={
                                 "Authorization": "Basic YWRtaW46YWRtaW4="},

                             )
    assert response.status_code == 200
    print(response.json())

    app.dependency_overrides = {}


def test_update_prophecy(client, get_test_session_engine):
    app.dependency_overrides[get_session] = get_test_session_engine

    response = client.patch("/api/prophecy",
                            headers={"Authorization": "Basic YWRtaW46YWRtaW4="},
                            json={"content": "вызов"},
                            params={"id": 1}
                            )
    print(response.json())
    assert response.status_code == 200

    app.dependency_overrides = {}
