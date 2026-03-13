import pytest
from app import create_app

@pytest.fixture
def client():
    # Crée l'instance de l'application pour les tests
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Vérifie que la route de santé répond 200"""
    response = client.get('/healthz')
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}

def test_ready_check(client):
    """Vérifie que la route de disponibilité répond 200"""
    response = client.get('/readyz')
    assert response.status_code == 200
    assert response.get_json() == {"status": "ready"}

def test_api_events(client):
    """Vérifie que la route API events répond avec la clé 'items'"""
    response = client.get('/api/events')
    assert response.status_code == 200
    data = response.get_json()
    assert "items" in data
    assert "category" in data
    assert data["category"] == "events"

def test_api_news(client):
    """Vérifie que la route API news est accessible"""
    response = client.get('/api/news')
    assert response.status_code == 200

def test_api_faq(client):
    """Vérifie que la route API faq est accessible"""
    response = client.get('/api/faq')
    assert response.status_code == 200
