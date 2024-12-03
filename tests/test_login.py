import requests
import pytest
import allure

BASE_URL = "https://stellarburgers.nomoreparties.site/api"

@pytest.fixture
def login_data():
    return {
        "email": "test-user@example.com",
        "password": "password123"
    }

class TestLogin:

    @allure.feature("Логин пользователя")
    @allure.story("Успешный логин")
    def test_login_success(self, login_data):
        response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
        assert response.status_code == 200
        assert "accessToken" in response.json()

    @allure.feature("Логин пользователя")
    @allure.story("Неуспешный логин с неверными данными")
    def test_login_failure(self):
        login_data = {"email": "wrong_user123@example.com", "password": "wrong_password123"}
        response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"
