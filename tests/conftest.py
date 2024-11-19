import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.fixture
def app():
    return APIClient()


@pytest.fixture
def user():
    """
    Fixture per creare un utente fittizio.
    """
    User = get_user_model()
    return User.objects.create_user(
        username="testuser",
        email="testuser@example.com",
        password="securepassword123"
    )