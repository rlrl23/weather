from __future__ import annotations

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get('/')
    assert response.status_code == 200


def test_read_weather_page():
    response = client.post('/weather', data={'city_name': 'Москва'})
    assert response.status_code == 200


def test_history():
    response = client.get('/history')
    assert response.status_code == 200
    assert response.json() == {'Москва': 1}
