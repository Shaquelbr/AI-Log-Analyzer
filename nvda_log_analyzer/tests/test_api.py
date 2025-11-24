from fastapi.testclient import TestClient
from analyzer.api import app

def test_api_analyze():
    client = TestClient(app)

    response = client.post("/analyze", json={
        "log_text": "ERROR Something broke"

    })

    assert response.status_code == 200
    data = response.json()
    assert "result" in data

    