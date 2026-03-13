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
        "password": "83r5^_"
    }

    response = client.post(LOGIN, credentials)

    data = response.json()

    token = data["token"]

    return token

@pytest.fixture
def auth_client(client, auth_token):

    client.session.headers.update(
        {
            "Authorization": f"Bearer {auth_token}"
        }
    )

    return client