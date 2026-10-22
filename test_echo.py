import requests
import pytest
from conftest import ECHO_URL

def test_positive_get_method_query_params():
    """
    Проверка GET-запроса с валидными query-параметрами.
    """
    response = requests.get(
        f'{ECHO_URL}/get?name=Aleksandr&age=28'
    )
    assert response.status_code == 200
    assert response.json()['args'] == {
        'name': 'Aleksandr',
        'age': '28'
    }

def test_get_method_query_params_with_special_symbol():
    """
    Проверка обработки спец. символов в query-параметрах
    """
    response = requests.get(
        f'{ECHO_URL}/get?symbol=!#$%^'
    )
    assert response.status_code == 200
    assert response.json()['args'] == {'symbol': '!'}

def test_post_method_with_get_in_url():
    """
    Проверка отправки POST-запроса на endpoint, поддерживающий только GET-запросы
    """
    response = requests.post(
        f'{ECHO_URL}/get'
    )
    assert response.status_code == 404

def test_post_method_json(user_payload):
    """
    Проверка отправки JSON тела в POST-запросе
    """
    response = requests.post(
        f'{ECHO_URL}/post',
        json=user_payload
    )
    assert response.status_code == 200
    assert response.json()['json'] == user_payload

def test_post_method_empty_json():
    """
    Проверка обработки пустого JSON
    """
    payload = {}
    response = requests.post(f'{ECHO_URL}/post', json=payload)
    assert response.status_code == 200
    assert response.json()['json'] == None
