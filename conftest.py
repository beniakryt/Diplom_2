import requests
import pytest

BASE_URL = "https://stellarburgers.nomoreparties.site/api"

@pytest.fixture
def auth_token():
    login_data = {
        "email": "yuriibenia@example.com",
        "password": "password123",
        "name": "yurii"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
    assert response.status_code == 200

    token = response.json()['accessToken']
    return token.replace("Bearer ", "")


@pytest.fixture
def auth_header(auth_token):
    return {"Authorization": f"Bearer {auth_token}"}

@pytest.fixture
def order_data():
    return {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70"]
    }
