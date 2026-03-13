import pytest

from api.api_client import APIClient
from api.endpoints import LOGIN


@pytest.fixture(scope="session")
def client():

    return APIClient()


@pytest.fixture(scope="session")
def auth_token(client):

    credentials = {
        "username": "mor_2314",
        "password": "83r5^_",
    }

    response = client.post(LOGIN, credentials)

    token = None

    if response.status_code in [200, 201]:

        try:
            data = response.json()
            token = data.get("token")
        except Exception:
            token = None

    # return None if login blocked
    return token


@pytest.fixture
def auth_client(client, auth_token):

    # only add header if token exists
    if auth_token:

        client.session.headers.update(
            {
                "Authorization": f"Bearer {auth_token}"
            }
        )

    return client