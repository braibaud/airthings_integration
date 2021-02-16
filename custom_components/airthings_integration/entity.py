"""AirthingsIntegrationEntity class"""
from typing import Any, Dict
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

from .const import ATTRIBUTION, DEVICE_BATTERY
from .const import DOMAIN
from .const import NAME
from .const import VERSION

ata = __import__("airthings-api")


class AirthingsIntegrationEntity(CoordinatorEntity):
    def __init__(
        self,
        coordinator: DataUpdateCoordinator[Any],
        location: ata.responses.locations_instance.Location,
        device: ata.responses.locations_instance.Device,
        sensor: ata.responses.locations_instance.CurrentSensorValue,
    ) -> None:
        super().__init__(coordinator)
        self.location = location
        self.device = device
        self.sensor = sensor

    @property
    def unique_id(self) -> str:
        """Return a unique ID to use for this entity."""
        return "{0}-{1}-{2}".format(
            self.location.id_, self.device.serial_number, self.sensor_type
        ).lower()

    @property
    def sensor_type(self) -> str:
        if self.sensor is None:
            return DEVICE_BATTERY
        else:
            return self.sensor.type_

    @property
    def sensor_units(self) -> str:
        if self.sensor is None:
            return "%"
        else:
            return self.sensor.provided_unit

    @property
    def device_unique_id(self) -> str:
        """Return a unique ID to use for the entity device."""
        return "{0}-{1}".format(self.location.id_, self.device.serial_number).lower()

    @property
    def device_info(self) -> Dict[str, Any]:
        return {
            "identifiers": {(DOMAIN, self.device_unique_id)},
            "name": "{0}-{1}".format(self.location.name, self.device.room_name).lower(),
            "model": self.device.type_,
            "manufacturer": "AirThings",
        }

    @property
    def device_state_attributes(self) -> Dict[str, Any]:
        """Return the state attributes."""
        return {
            "attribution": ATTRIBUTION,
            "id": self.sensor_type,
            "integration": DOMAIN,
        }
