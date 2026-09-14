from app import app


def test_root():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["service"] == "devops-health-api"


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"
