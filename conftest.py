import pytest

ECHO_URL = 'https://postman-echo.com'

@pytest.fixture
def user_payload():
    return {
        "name": "Aleksandr",
        "age": 28,
        "isStudent": True,
        "empty": ""
    }