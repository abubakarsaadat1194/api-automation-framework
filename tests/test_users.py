import pytest

from api.endpoints import USERS, USER_BY_ID
from utils.assertions import (
    assert_status,
    assert_status_in,
    assert_type,
    assert_key,
    assert_not_empty,
    safe_json,
)

from utils.data_loader import load_json


users_data = load_json("users.json")


def test_get_users(auth_client):

    response = auth_client.get(USERS)

    data = safe_json(response)

    assert_status(response, 200)

    if response.status_code == 200:
        assert_type(data, list)
        assert_not_empty(data)


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user_by_id(auth_client, user_id):

    response = auth_client.get(USER_BY_ID(user_id))

    data = safe_json(response)

    assert_status(response, 200)

    if response.status_code == 200:
        assert_type(data, dict)
        assert_key(data, "id")
        assert data["id"] == user_id


@pytest.mark.parametrize("user", users_data)
def test_create_user(auth_client, user):

    response = auth_client.post(USERS, user)

    data = safe_json(response)

    assert_status_in(response, [200, 201])

    # FakeStore returns only id
    if response.status_code in [200, 201]:
        assert_key(data, "id")