"""Tests for airthings-integration api."""
import os

from custom_components.airthings_integration.api import AirthingsIntegrationApiClient
from homeassistant.helpers.aiohttp_client import async_get_clientsession


AIRTHINGS_USERNAME = os.environ.get("AIRTHINGS_USERNAME")
AIRTHINGS_PASSWORD = os.environ.get("AIRTHINGS_PASSWORD")

AIRTHINGS_USERNAME_WRONG = "AIRTHINGS_USERNAME"
AIRTHINGS_PASSWORD_WRONG = "AIRTHINGS_PASSWORD"


async def test__validate_credentials(hass):
    """Test API connectivity (positive testing)."""

    # To test the api submodule, we first create an instance of our API client
    api = AirthingsIntegrationApiClient(
        username=AIRTHINGS_USERNAME,
        password=AIRTHINGS_PASSWORD,
        session=async_get_clientsession(hass),
    )

    # Ensure connection is successful
    assert await api.manager.validate_credentials()


async def test__invalidate_wrong_credentials(hass):
    """Test API connectivity (negative testing)."""

    # To test the api submodule, we first create an instance of our API client
    api = AirthingsIntegrationApiClient(
        username=AIRTHINGS_USERNAME_WRONG,
        password=AIRTHINGS_PASSWORD_WRONG,
        session=async_get_clientsession(hass),
    )

    # Ensure connection is successful
    result = await api.manager.validate_credentials()
    assert not result
