import requests
import allure
from data.constants import BASE_URL, ERROR_MESSAGES
from data.endpoints import ENDPOINTS

@allure.feature("Получение заказов")
class TestGetOrders:

    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_orders_with_auth(self, auth_header):
        response = requests.get(f"{BASE_URL}{ENDPOINTS['orders']}", headers=auth_header)
        assert response.status_code == 200
        assert "orders" in response.json()

    @allure.title("Попытка получить заказы без авторизации")
    def test_get_orders_without_auth(self):
        response = requests.get(f"{BASE_URL}{ENDPOINTS['orders']}")
        assert response.status_code == 401
        assert response.json()["message"] == ERROR_MESSAGES["unauthorized"]
