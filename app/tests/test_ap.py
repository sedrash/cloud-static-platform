import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/healthz')
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}

def test_api_events(client):
    response = client.get('/api/events')
    assert response.status_code == 200
    data = response.get_json()
    # On vérifie que la structure corrigée est bien présente
    assert "items" in data
    assert "category" in data
    assert data["category"] == "events"
