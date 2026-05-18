# devices/climate.py  –  Thermostat / HVAC
from ha_client.client import call_service, get_state


def set_temperature(entity_id: str, temperature: float):
    return call_service("climate", "set_temperature", entity_id, temperature=temperature)


def set_hvac_mode(entity_id: str, mode: str):
    """mode: 'heat' | 'cool' | 'heat_cool' | 'auto' | 'off'"""
    return call_service("climate", "set_hvac_mode", entity_id, hvac_mode=mode)


def get_temperature(entity_id: str) -> dict:
    s = get_state(entity_id)
    attrs = s.get("attributes", {})
    return {
        "current": attrs.get("current_temperature"),
        "target": attrs.get("temperature"),
        "mode": s["state"],
    }