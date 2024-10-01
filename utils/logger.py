import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def log(response, json=None):
    logger.info(f"Method:{response.request.method}")
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Request Headers:{response.request.headers}")
    logger.info(f"Request Body: {json}")
    logger.info(f"Response Headers: {response.headers}")
    logger.info(f"Response Body: {response.text}")
