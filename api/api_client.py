import requests
import json

from utils.config import BASE_URL
from utils.logger import get_logger


logger = get_logger("APIClient")


class APIClient:

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update(
            {
                "Content-Type": "application/json",
                "User-Agent": "pytest-api-framework",
            }
        )

    def _log_response(self, response):

        logger.info(f"URL: {response.request.method} {response.url}")
        logger.info(f"Status: {response.status_code}")

        # try JSON first
        try:

            data = response.json()

            logger.info("Response JSON:")
            logger.info(json.dumps(data, indent=2))

        except Exception:

            logger.info("No JSON response")
            logger.info("Response text:")
            logger.info(response.text[:300])  # limit size

    def get(self, endpoint):

        url = BASE_URL + endpoint

        response = self.session.get(url)

        self._log_response(response)

        return response

    def post(self, endpoint, data):

        url = BASE_URL + endpoint

        logger.info(f"POST Payload: {data}")

        response = self.session.post(url, json=data)

        self._log_response(response)

        return response

    def put(self, endpoint, data):

        url = BASE_URL + endpoint

        logger.info(f"PUT Payload: {data}")

        response = self.session.put(url, json=data)

        self._log_response(response)

        return response

    def delete(self, endpoint):

        url = BASE_URL + endpoint

        response = self.session.delete(url)

        self._log_response(response)

        return response