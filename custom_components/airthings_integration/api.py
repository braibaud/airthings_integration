"""Sample API Client."""
import asyncio
import logging
import socket

import aiohttp
import async_timeout

ata = __import__('airthings-api')

TIMEOUT = 10


_LOGGER: logging.Logger = logging.getLogger(__package__)

HEADERS = {"Content-type": "application/json; charset=UTF-8"}


class AirthingsIntegrationApiClient:
    def __init__(
        self, username: str, password: str, session: aiohttp.ClientSession
    ) -> None:
        self.manager = ata.api.web.AirThingsManager(
            username=username,
            password=password,
            session=session)
