import requests
import allure

BASE_URL = "https://stellarburgers.nomoreparties.site/api"

class TestGetOrders:

    @allure.feature("Получение заказов")
    @allure.story("Получение заказов авторизованного пользователя")
    def test_get_orders_with_auth(self, auth_header):
        response = requests.get(f"{BASE_URL}/orders", headers=auth_header)
        assert response.status_code == 200
        assert "orders" in response.json()

    @allure.feature("Получение заказов")
    @allure.story("Попытка получить заказы без авторизации")
    def test_get_orders_without_auth(self):
        response = requests.get(f"{BASE_URL}/orders")
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"