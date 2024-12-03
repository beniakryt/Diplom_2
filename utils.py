import random
import string

def generate_unique_email():
    """Генерация уникального email для теста"""
    unique_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))  # Генерация 8 случайных символов
    return f"test-user-{unique_part}@example.com"
