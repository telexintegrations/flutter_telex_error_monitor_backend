import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock
from main import app

client = TestClient(app)


def test_get_integration_json():

    response = client.get("/api/integration.json")
    assert response.status_code == 200
    data = response.json()

    assert "data" in data
    assert data["data"]["descriptions"]["app_name"] == "Flutter Telex Error Monitor"
    assert data["data"]["integration_type"] == "modifier"


@pytest.mark.asyncio
async def test_submit_error(mocker):

    mock_post = mocker.patch("httpx.AsyncClient.post", new_callable=AsyncMock)
    mock_post.return_value.status_code = 200

    error_payload = {
        "app_name": "Test App",
        "error": "Null Pointer Exception",
        "location": "<fn>MainActivity</fn>",
        "telex_channel_webhook_Url": "https://mock.telex.api/webhook"
    }

    response = client.post("/api/v1/submit-error", json=error_payload)

    assert response.status_code == 200
    assert response.json() == {"status": "success"}

    mock_post.assert_called_once_with(
        "https://mock.telex.api/webhook",
        json={
            "event_name": "Flutter Telex Error Monitor",
            "message": "Error: Null Pointer Exception\n    Location: MainActivity",
            "status": "success",
            "username": "Test App"
        },
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    )