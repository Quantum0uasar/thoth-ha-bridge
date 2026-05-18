# devices/switch.py  –  Switch / plug controls
from ha_client.client import call_service, get_state


def turn_on(entity_id: str):
    return call_service("switch", "turn_on", entity_id)


def turn_off(entity_id: str):
    return call_service("switch", "turn_off", entity_id)


def toggle(entity_id: str):
    return call_service("switch", "toggle", entity_id)


def is_on(entity_id: str) -> bool:
    return get_state(entity_id)["state"] == "on"