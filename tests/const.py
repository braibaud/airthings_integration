"""Constants for airthings-integration tests."""
import os

VALID_CONFIG = {
    "username": os.environ.get("AIRTHINGS_USERNAME"),
    "password": os.environ.get("AIRTHINGS_PASSWORD"),
}

INVALID_CONFIG = {
    "username": "test_username",
    "password": "test_password",
}
