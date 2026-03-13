import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_health(client):
    response = client.get('/healthz')
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}

def test_ready(client):
    response = client.get('/readyz')
    assert response.status_code == 200
    assert response.get_json() == {"status": "ready"}

def test_api_events(client):
    response = client.get('/api/events')
    assert response.status_code == 200
    data = response.get_json()
    assert "items" in data
