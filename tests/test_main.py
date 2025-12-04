from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_echo():
    r = client.post("/echo", json={"message": "DevOps"})
    assert r.status_code == 200
    assert r.json()["you_said"] == "DevOps"
    assert r.json()["length"] == 6

def test_version():
    r = client.get("/version")
    assert r.status_code == 200
    assert "version" in r.json()
    assert "github" in r.json()