import requests
import allure
from data.constants import BASE_URL, ERROR_MESSAGES
from data.endpoints import ENDPOINTS

@allure.feature("Изменение данных пользователя")
class TestUpdateUser:

    @allure.title("Изменение данных с авторизацией")
    def test_update_user_with_auth(self, auth_header):
        response = requests.patch(
            f"{BASE_URL}{ENDPOINTS['user']}",
            json={"name": "Updated User Name"},
            headers=auth_header
        )
        assert response.status_code == 200
        assert response.json()["user"]["name"] == "Updated User Name"

    @allure.title("Попытка изменить данные без авторизации")
    def test_update_user_without_auth(self):
        response = requests.patch(
            f"{BASE_URL}{ENDPOINTS['user']}",
            json={"name": "Unauthorized Update"}
        )
        assert response.status_code == 401
        assert response.json()["message"] == ERROR_MESSAGES["unauthorized"]
