import requests
import allure
from utils import generate_unique_email

BASE_URL = "https://stellarburgers.nomoreparties.site/api"

class TestCreateUser:

    @allure.feature("Создание пользователя")
    @allure.story("Уникальная регистрация пользователя")
    def test_create_unique_user(self):
        user_data = {
            "email": generate_unique_email(),
            "password": "password123",
            "name": "Test User"
        }
        response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
        assert response.status_code == 200
        assert "user" in response.json()
        assert response.json()["user"]["email"] == user_data["email"]

    @allure.feature("Создание пользователя")
    @allure.story("Попытка зарегистрировать уже существующего пользователя")
    def test_create_existing_user(self):
        existing_user_data = {
            "email": "yuriibenia@example.com",
            "password": "password123",
            "name": "TestUser"
        }

        response = requests.post(f"{BASE_URL}/auth/register", json=existing_user_data)
        assert response.status_code == 403
        assert response.json().get("message") == "User already exists"

    @allure.feature("Создание пользователя")
    @allure.story("Попытка зарегистрировать пользователя без обязательного поля")
    def test_create_user_without_required_field(self):
        user_data = {"password": "password123", "name": "NoEmailUser"}
        response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"
