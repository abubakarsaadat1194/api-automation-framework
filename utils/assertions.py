import os


def assert_status(response, expected):

    # allow 403 in CI (Cloudflare block)
    if os.getenv("CI") == "true" and response.status_code == 403:
        return

    assert response.status_code == expected, (
        f"Expected status {expected}, got {response.status_code}"
    )


def assert_status_in(response, expected_list):

    # allow 403 in CI
    if os.getenv("CI") == "true" and response.status_code == 403:
        return

    assert response.status_code in expected_list, (
        f"Expected status in {expected_list}, got {response.status_code}"
    )


def assert_key(data, key):

    assert key in data, f"Key '{key}' not found"


def assert_type(data, expected_type):

    assert isinstance(data, expected_type), (
        f"Expected {expected_type}, got {type(data)}"
    )


def assert_not_empty(data):

    assert len(data) > 0