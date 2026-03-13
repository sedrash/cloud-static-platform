import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Vérifie que la route de santé fonctionne (Source 39)"""
    response = client.get('/healthz')
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}

def test_api_events(client):
    """Vérifie que l'API events retourne la bonne structure (Source 143)"""
    response = client.get('/api/events')
    assert response.status_code == 200
    data = response.get_json()
    assert "items" in data  # Vérifie la présence de la clé items
