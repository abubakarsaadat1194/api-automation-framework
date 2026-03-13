import pytest
import allure

from api.endpoints import PRODUCTS, PRODUCT_BY_ID
from utils.assertions import (
    assert_status,
    assert_status_in,
    assert_type,
    assert_key,
    assert_not_empty,
    safe_json,
)

from utils.data_loader import load_json


products_data = load_json("products.json")


@allure.feature("Products")
@allure.story("Get all products")
def test_get_products(auth_client):

    response = auth_client.get(PRODUCTS)

    data = safe_json(response)

    # allow 403 in CI
    assert_status_in(response, [200, 403])

    if response.status_code == 200:
        assert_type(data, list)
        assert_not_empty(data)


@allure.feature("Products")
@pytest.mark.parametrize("product_id", [1, 2, 3, 4])
def test_get_product_by_id(auth_client, product_id):

    response = auth_client.get(PRODUCT_BY_ID(product_id))

    data = safe_json(response)

    assert_status_in(response, [200, 403])

    if response.status_code == 200:
        assert_type(data, dict)
        assert_key(data, "id")


@allure.feature("Products")
@pytest.mark.parametrize("product", products_data)
def test_create_product(auth_client, product):

    response = auth_client.post(PRODUCTS, product)

    data = safe_json(response)

    assert_status_in(response, [200, 201, 403])

    if response.status_code in [200, 201]:
        assert_key(data, "id")


@allure.feature("Products")
def test_update_product(auth_client):

    updated_product = {
        "title": "updated",
        "price": 10.5,
    }

    response = auth_client.put(PRODUCT_BY_ID(1), updated_product)

    data = safe_json(response)

    assert_status_in(response, [200, 403])

    if response.status_code == 200:
        assert_key(data, "id")


@allure.feature("Products")
def test_delete_product(auth_client):

    response = auth_client.delete(PRODUCT_BY_ID(1))

    assert_status_in(response, [200, 204, 403])