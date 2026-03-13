import pytest
import allure

from api.endpoints import PRODUCTS, PRODUCT_BY_ID
from utils.assertions import (
    assert_status,
    assert_status_in,
    assert_type,
    assert_key,
    assert_not_empty,
)

from utils.data_loader import load_json


products_data = load_json("products.json")


@allure.feature("Products")
@allure.story("Get all products")
@allure.severity(allure.severity_level.NORMAL)
def test_get_products(auth_client):

    with allure.step("Send GET /products"):
        response = auth_client.get(PRODUCTS)

    with allure.step("Validate response"):
        data = response.json()

        assert_status(response, 200)
        assert_type(data, list)
        assert_not_empty(data)


@allure.feature("Products")
@allure.story("Get product by id")
@pytest.mark.parametrize("product_id", [1, 2, 3, 4])
def test_get_product_by_id(auth_client, product_id):

    with allure.step(f"Send GET /products/{product_id}"):

        response = auth_client.get(PRODUCT_BY_ID(product_id))

    data = response.json()

    assert_status(response, 200)
    assert_type(data, dict)
    assert_key(data, "id")

    assert data["id"] == product_id


@allure.feature("Products")
@allure.story("Create product")
@pytest.mark.parametrize("product", products_data)
def test_create_product(auth_client, product):

    with allure.step("Send POST /products"):

        response = auth_client.post(PRODUCTS, product)

    data = response.json()

    assert_status_in(response, [200, 201])
    assert_key(data, "id")


@allure.feature("Products")
@allure.story("Update product")
def test_update_product(auth_client):

    updated_product = {
        "title": "updated product created by Abu Bakar",
        "price": 10.5,
    }

    with allure.step("Send PUT /products/1"):

        response = auth_client.put(PRODUCT_BY_ID(1), updated_product)

    data = response.json()

    assert_status(response, 200)
    assert_key(data, "id")


@allure.feature("Products")
@allure.story("Delete product")
def test_delete_product(auth_client):

    with allure.step("Send DELETE /products/1"):

        response = auth_client.delete(PRODUCT_BY_ID(1))

    assert_status_in(response, [200, 204])