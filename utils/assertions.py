def assert_status(response, expected):

    assert response.status_code == expected, (
        f"Expected status {expected}, got {response.status_code}"
    )


def assert_status_in(response, expected_list):

    assert response.status_code in expected_list, (
        f"Expected status in {expected_list}, got {response.status_code}"
    )


def assert_key(data, key):

    assert key in data, f"Key '{key}' not found in response"


def assert_type(data, expected_type):

    assert isinstance(data, expected_type), (
        f"Expected type {expected_type}, got {type(data)}"
    )


def assert_not_empty(data):

    assert len(data) > 0, "Response is empty"