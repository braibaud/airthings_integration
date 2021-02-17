"""Sensor platform for airthings_integration."""
from .const import DEVICE_BATTERY
from .const import DOMAIN
from .const import ICON
from .entity import AirthingsIntegrationEntity


async def async_setup_entry(hass, entry, async_add_devices):

    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    sensors = []

    for location in coordinator.data.locations:
        for device in location.devices:

            # Add the battery level if available
            if device.battery_percentage is not None:
                sensors.append(
                    AirthingsIntegrationSensor(
                        coordinator=coordinator,
                        location=location,
                        device=device,
                        sensor=None,
                    )
                )

            # Add all the available sensors
            for sensor in device.current_sensor_values:
                sensors.append(
                    AirthingsIntegrationSensor(
                        coordinator=coordinator,
                        location=location,
                        device=device,
                        sensor=sensor,
                    )
                )

    async_add_devices(sensors)


class AirthingsIntegrationSensor(AirthingsIntegrationEntity):
    """airthings_integration Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return "{0}-{1}-{2}".format(
            self.location.name, self.device.room_name, self.sensor_type
        ).lower()

    @property
    def state(self):
        """Return the state of the sensor."""
        result = None
        for location in self.coordinator.data.locations:
            if location.id_ == self.location.id_:
                for device in location.devices:
                    if device.serial_number == self.device.serial_number:
                        if self.sensor_type == DEVICE_BATTERY:
                            result = device.battery_percentage
                        else:
                            for sensor in device.current_sensor_values:
                                if sensor.type_ == self.sensor_type:
                                    result = sensor.value
        return result

    @property
    def icon(self):
        """Return the icon of the sensor."""
        if self.sensor_type == "radonShortTermAvg":
            return "mdi:radioactive"
        elif self.sensor_type == "temp":
            return "mdi:thermometer"
        elif self.sensor_type == "humidity":
            return "mdi:water-percent"
        elif self.sensor_type == "mold":
            return "mdi:mushroom"
        elif self.sensor_type == "voc":
            return "mdi:chemical-weapon"
        elif self.sensor_type == DEVICE_BATTERY:
            if self.device.battery_percentage > 60:
                return "mdi:battery-high"
            elif self.device.battery_percentage > 30:
                return "mdi:battery-medium"
            else:
                return "mdi:battery-low"

        return ICON

    @property
    def device_class(self):
        """Return de device class of the sensor."""
        if self.sensor_type == "temp":
            return "temperature"
        elif self.sensor_type == "humidity":
            return "humidity"
        elif self.sensor_type == DEVICE_BATTERY:
            return "battery"

        return "airthings_integration__custom_device_class"

    @property
    def unit_of_measurement(self):
        """Defines the units of measurement, if any."""
        return self.sensor_units
