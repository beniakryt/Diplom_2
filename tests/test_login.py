import requests
import allure
from data.constants import BASE_URL, ERROR_MESSAGES
from data.endpoints import ENDPOINTS
from data.test_data import USER_DATA

@allure.feature("Логин пользователя")
class TestLogin:

    @allure.title("Успешный логин")
    def test_login_success(self):
        response = requests.post(f"{BASE_URL}{ENDPOINTS['login']}", json=USER_DATA["valid_user"])
        assert response.status_code == 200
        assert "accessToken" in response.json()
        assert response.json()["user"]["email"] == USER_DATA["valid_user"]["email"]

    @allure.title("Неуспешный логин с неверными данными")
    def test_login_failure(self):
        response = requests.post(f"{BASE_URL}{ENDPOINTS['login']}", json=USER_DATA["invalid_user"])
        assert response.status_code == 401
        assert response.json()["message"] == ERROR_MESSAGES["invalid_credentials"]
