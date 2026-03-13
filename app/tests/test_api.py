from app import create_app

app = create_app()
client = app.test_client()


def test_health():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_ready():
    response = client.get("/readyz")
    assert response.status_code == 200


def test_events():
    response = client.get("/api/events")
    assert response.status_code == 200


def test_news():
    response = client.get("/api/news")
    assert response.status_code == 200


def test_faq():
    response = client.get("/api/faq")
    assert response.status_code == 200