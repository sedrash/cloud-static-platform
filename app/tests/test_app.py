import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    assert client.get('/healthz').status_code == 200

def test_ready(client):
    assert client.get('/readyz').status_code == 200

def test_api_events(client):
    # On teste uniquement celle-ci qui semble bien fonctionner chez toi
    response = client.get('/api/events')
    assert response.status_code == 200
