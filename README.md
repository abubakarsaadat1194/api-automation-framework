# API Automation Framework (Python + Pytest + Requests)

This project is a REST API automation framework built using Python, Pytest, and Requests.
It demonstrates how to design a clean, scalable, and reusable API test framework similar to real industry projects.

The framework tests the public API:
https://fakestoreapi.com


--------------------------------------------------

PROJECT FEATURES

- Pytest test framework
- Requests for API calls
- Fixture-based API client
- Authentication fixture
- Custom assertion helpers
- JSON test data
- Parametrized tests
- Dynamic endpoints
- Logging support
- GitHub Actions ready
- Clean project structure


--------------------------------------------------

PROJECT STRUCTURE

api-automation-framework

api/
    api_client.py
    endpoints.py

tests/
    test_login.py
    test_users.py
    test_products.py

utils/
    assertions.py
    data_loader.py
    logger.py

data/
    users.json
    products.json
    login.json

pytest.ini
requirements.txt
README.md
.gitignore


--------------------------------------------------

INSTALLATION

Clone repository

git clone https://github.com/YOUR_USERNAME/api-automation-framework.git

cd api-automation-framework


Create virtual environment

python3 -m venv venv

source venv/bin/activate


Install dependencies

pip install -r requirements.txt


--------------------------------------------------

RUN TESTS

Run all tests

pytest

Run with verbose

pytest -v


--------------------------------------------------

TEST DATA

Test data is stored in JSON files inside the data folder.

Example:

data/users.json
data/products.json
data/login.json

Data is loaded using:

utils/data_loader.py


--------------------------------------------------

ASSERTIONS HELPER

Custom assertions are stored in:

utils/assertions.py

Example functions:

assert_status(response, 200)

assert_status_in(response, [200, 201])

assert_key(data, "id")

assert_not_empty(data)


--------------------------------------------------

API CLIENT

All requests are handled by:

api/api_client.py

Supports:

GET
POST
PUT
DELETE

Also logs:

URL
Status
Response


--------------------------------------------------

ENDPOINTS

All endpoints are stored in:

api/endpoints.py


Example:

PRODUCTS = "/products"

def PRODUCT_BY_ID(id):
    return f"/products/{id}"


This allows dynamic requests.


--------------------------------------------------

PARAMETRIZED TESTS

Tests use pytest parametrize.

Example:

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user_by_id(...)


JSON data can also be used:

users_data = load_json("users.json")

@pytest.mark.parametrize("user", users_data)


--------------------------------------------------

AUTH FIXTURE

Login token is created once using fixture.

Used in:

conftest.py


--------------------------------------------------

LOGGING

Logging is implemented in:

utils/logger.py

Each request logs:

URL
Status
Response


--------------------------------------------------

GITHUB ACTIONS

CI workflow can run tests automatically on push.

Workflow file:

.github/workflows/tests.yml


--------------------------------------------------

API USED

Fake Store API

https://fakestoreapi.com


--------------------------------------------------

AUTHOR

Abu Bakar Saadat

QA Automation Engineer

Python | Pytest | Playwright | API Testing | Selenium | 5G | LTE