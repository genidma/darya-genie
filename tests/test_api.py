import pytest
from httpx import AsyncClient, ASGITransport
from src.api.main import app

@pytest.fixture
def client():
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")

@pytest.mark.asyncio
async def test_health_check(client):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

@pytest.mark.asyncio
async def test_submit_restoration_success(client):
    headers = {"token": "token-abc-123"}
    payload = {
        "coordinates": [25.0, 55.0],
        "species": "Rhizophora mucronata",
        "quantity": 10,
        "bounty": 5.0
    }
    response = await client.post("/api/v1/submit_restoration", json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "tx_id" in data
    assert data["amount"] == 5.0

@pytest.mark.asyncio
async def test_submit_restoration_unauthorized(client):
    headers = {"token": "token-def-456"}  # not certified
    payload = {
        "coordinates": [25.0, 55.0],
        "species": "Avicennia marina",
        "quantity": 5,
        "bounty": 2.5
    }
    response = await client.post("/api/v1/submit_restoration", json=payload, headers=headers)
    assert response.status_code == 403
    assert response.json()["detail"] == "Certification Required"

@pytest.mark.asyncio
async def test_submit_restoration_invalid_site(client):
    headers = {"token": "token-abc-123"}
    payload = {
        "coordinates": [30.0, 50.0],  # not in suitable sites
        "species": "Bruguiera gymnorhiza",
        "quantity": 3,
        "bounty": 1.5
    }
    response = await client.post("/api/v1/submit_restoration", json=payload, headers=headers)
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid Planting Site"

@pytest.mark.asyncio
async def test_submit_waste_collection_success(client):
    headers = {"token": "token-abc-123"}
    payload = {
        "gps_coordinates": [25.2, 55.3],
        "photo_url": "https://example.com/photo.jpg",
        "waste_type": "plastic",
        "estimated_volume": 10.0
    }
    response = await client.post("/api/v1/submit_waste_collection", json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["amount"] == 5.0  # 10 * 0.5

@pytest.mark.asyncio
async def test_submit_waste_collection_anti_gaming_fail(client):
    headers = {"token": "token-abc-123"}
    payload = {
        "gps_coordinates": [25.2, 55.3],
        "photo_url": "https://fake.example.com/photo.jpg",  # triggers anti-gaming
        "waste_type": "metal",
        "estimated_volume": 5.0
    }
    response = await client.post("/api/v1/submit_waste_collection", json=payload, headers=headers)
    assert response.status_code == 400
    assert "anti-gaming" in response.json()["detail"].lower()

@pytest.mark.asyncio
async def test_missing_token(client):
    payload = {
        "coordinates": [25.0, 55.0],
        "species": "Test",
        "quantity": 1,
        "bounty": 1.0
    }
    response = await client.post("/api/v1/submit_restoration", json=payload)
    assert response.status_code == 422  # validation error for missing header
