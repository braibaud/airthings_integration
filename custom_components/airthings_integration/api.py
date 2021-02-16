"""Sample API Client."""
import logging

import aiohttp

ata = __import__("airthings-api")

TIMEOUT = 10


_LOGGER: logging.Logger = logging.getLogger(__package__)

HEADERS = {"Content-type": "application/json; charset=UTF-8"}


class AirthingsIntegrationApiClient:
    def __init__(
        self, username: str, password: str, session: aiohttp.ClientSession
    ) -> None:
        self.manager = ata.api.web.AirThingsManager(
            username=username, password=password, session=session
        )
