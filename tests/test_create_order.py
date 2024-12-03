import requests
import allure
from data.constants import BASE_URL, ERROR_MESSAGES
from data.endpoints import ENDPOINTS
from data.test_data import ORDER_DATA

@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, auth_header):
        response = requests.post(
            f"{BASE_URL}{ENDPOINTS['orders']}",
            json={"ingredients": ORDER_DATA["valid_ingredients"]},
            headers=auth_header
        )
        assert response.status_code == 200
        assert "order" in response.json()

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self):
        response = requests.post(
            f"{BASE_URL}{ENDPOINTS['orders']}",
            json={"ingredients": ORDER_DATA["valid_ingredients"]}
        )
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, auth_header):
        response = requests.post(
            f"{BASE_URL}{ENDPOINTS['orders']}",
            json={"ingredients": ORDER_DATA["valid_ingredients"]},
            headers=auth_header
        )
        assert response.status_code == 200
        assert "order" in response.json()

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, auth_header):
        response = requests.post(
            f"{BASE_URL}{ENDPOINTS['orders']}",
            json={"ingredients": []},
            headers=auth_header
        )
        assert response.status_code == 400
        assert response.json()["message"] == ERROR_MESSAGES["missing_ingredients"]

    @allure.title("Создание заказа с неверными хешами ингредиентов")
    def test_create_order_with_invalid_ingredients(self, auth_header):
        response = requests.post(
            f"{BASE_URL}{ENDPOINTS['orders']}",
            json={"ingredients": ORDER_DATA["invalid_ingredients"]},
            headers=auth_header
        )
        assert response.status_code == 400
        assert response.json()["message"] == ERROR_MESSAGES["invalid_ingredients"]
