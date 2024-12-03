import requests
import allure

BASE_URL = "https://stellarburgers.nomoreparties.site/api"

class TestUpdateUser:

    @allure.feature("Изменение данных пользователя")
    @allure.story("Изменение данных с авторизацией")
    def test_update_user_with_auth(self, auth_header):
        user_data = {"name": "Updated User Name"}
        response = requests.patch(f"{BASE_URL}/auth/user", json=user_data, headers=auth_header)
        assert response.status_code == 200
        assert response.json()["user"]["name"] == "Updated User Name"

    @allure.feature("Изменение данных пользователя")
    @allure.story("Изменение данных без авторизации")
    def test_update_user_without_auth(self):
        user_data = {"name": "yuriibenia"}
        response = requests.patch(f"{BASE_URL}/auth/user", json=user_data)
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"
