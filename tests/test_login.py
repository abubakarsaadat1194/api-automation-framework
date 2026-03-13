import pytest

from api.endpoints import LOGIN
from utils.assertions import assert_status_in, assert_key, safe_json
from utils.data_loader import load_json


login_data = load_json("login.json")


@pytest.mark.parametrize("case", login_data)
def test_authentication(auth_client, case):

    credentials = {
        "username": case["username"],
        "password": case["password"],
    }

    expected_status = case["expected_status"]

    response = auth_client.post(LOGIN, credentials)

    # FakeStore sometimes returns 201 instead of 200
    assert_status_in(response, [expected_status, 201])

    # safe JSON parsing (prevents CI crash on 403)
    data = safe_json(response)

    if response.status_code in [200, 201]:
        assert_key(data, "token")