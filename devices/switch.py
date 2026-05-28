# devices/switch.py – Switch / plug controls
from __future__ import annotations
from ha_client.client import call_service, get_state


def turn_on(entity_id: str) -> dict:
    """Turn on a switch or smart plug."""
    return call_service("switch", "turn_on", entity_id)


def turn_off(entity_id: str) -> dict:
    """Turn off a switch or smart plug."""
    return call_service("switch", "turn_off", entity_id)


def toggle(entity_id: str) -> dict:
    """Toggle a switch between on and off."""
    return call_service("switch", "toggle", entity_id)


def is_on(entity_id: str) -> bool:
    """Return True if the switch is currently on."""
    return get_state(entity_id)["state"] == "on"


def set_state(entity_id: str, *, on: bool) -> dict:
    """Convenience helper – turn on or off based on a bool.

    Args:
        entity_id: HA entity ID.
        on:        ``True`` to turn on, ``False`` to turn off.
    """
    return turn_on(entity_id) if on else turn_off(entity_id)
