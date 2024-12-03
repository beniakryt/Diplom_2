import requests
import allure
from utils import generate_unique_email
from data.constants import BASE_URL, ERROR_MESSAGES
from data.endpoints import ENDPOINTS
from data.test_data import USER_DATA

@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title("Уникальная регистрация пользователя")
    def test_create_unique_user(self):
        user_data = {
            "email": generate_unique_email(),
            "password": "password123",
            "name": "Test User"
        }
        response = requests.post(f"{BASE_URL}{ENDPOINTS['register']}", json=user_data)
        assert response.status_code == 200
        assert "user" in response.json()
        assert response.json()["user"]["email"] == user_data["email"]

    @allure.title("Попытка зарегистрировать существующего пользователя")
    def test_create_existing_user(self):
        response = requests.post(f"{BASE_URL}{ENDPOINTS['register']}", json=USER_DATA["valid_user"])
        assert response.status_code == 403
        assert response.json()["message"] == ERROR_MESSAGES["user_exists"]

    @allure.title("Попытка зарегистрировать пользователя без обязательного поля")
    def test_create_user_without_required_field(self):
        user_data = {"password": "password123", "name": "NoEmailUser"}
        response = requests.post(f"{BASE_URL}{ENDPOINTS['register']}", json=user_data)
        assert response.status_code == 403
        assert response.json()["message"] == ERROR_MESSAGES["missing_fields"]
