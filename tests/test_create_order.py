import requests
import allure

BASE_URL = "https://stellarburgers.nomoreparties.site/api"


class TestCreateOrder:

    @allure.feature("Создание заказа")
    @allure.story("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, order_data, auth_token):
        headers = {"Authorization": f"{auth_token}"}
        response = requests.post(f"{BASE_URL}/orders", json=order_data, headers=headers)

        assert response.status_code == 200
        assert "order" in response.json()

    @allure.feature("Создание заказа")
    @allure.story("Попытка создать заказ без авторизации")
    def test_create_order_without_auth(self, order_data):
        response = requests.post(f"{BASE_URL}/orders", json=order_data)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.feature("Создание заказа")
    @allure.story("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, auth_token):
        order_data = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70"]}
        headers = {"Authorization": f"{auth_token}"}
        response = requests.post(f"{BASE_URL}/orders", json=order_data, headers=headers)

        assert response.status_code == 200
        assert "order" in response.json()

    @allure.feature("Создание заказа")
    @allure.story("Попытка создать заказ без ингредиентов")
    def test_create_order_without_ingredients(self, auth_token):
        order_data = {"ingredients": []}
        headers = {"Authorization": f"{auth_token}"}
        response = requests.post(f"{BASE_URL}/orders", json=order_data, headers=headers)

        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.feature("Создание заказа")
    @allure.story("Попытка создать заказ с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredients(self, auth_token):
        order_data = {"ingredients": ["60d3b41abdacab0026a733c6", "609646e4dc916e00276b2870"]}
        headers = {"Authorization": f"{auth_token}"}
        response = requests.post(f"{BASE_URL}/orders", json=order_data, headers=headers)

        assert response.status_code == 400
        assert response.json()["message"] == "One or more ids provided are incorrect"
