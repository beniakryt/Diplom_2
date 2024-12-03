import requests
import pytest
from data.constants import BASE_URL
from data.test_data import USER_DATA, ORDER_DATA

@pytest.fixture
def auth_token():
    """Получение токена авторизации"""
    response = requests.post(f"{BASE_URL}/auth/login", json=USER_DATA["valid_user"])
    response.raise_for_status()  # Бросает исключение, если код ответа не 200
    token = response.json()['accessToken']
    return token.replace("Bearer ", "")

@pytest.fixture
def auth_header(auth_token):
    """Фикстура для заголовка с токеном"""
    return {"Authorization": f"Bearer {auth_token}"}

@pytest.fixture
def order_data():
    """Данные для создания заказа"""
    return {"ingredients": ORDER_DATA["valid_ingredients"]}
