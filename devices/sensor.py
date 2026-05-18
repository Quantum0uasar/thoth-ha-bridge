# devices/sensor.py  –  Read sensor values
from ha_client.client import get_state, get_states


def read(entity_id: str) -> dict:
    """Return state + attributes for any sensor entity."""
    s = get_state(entity_id)
    return {
        "entity_id": s["entity_id"],
        "value": s["state"],
        "unit": s.get("attributes", {}).get("unit_of_measurement", ""),
        "last_updated": s.get("last_updated"),
    }


def get_all_sensors() -> list:
    """Return a summary of every sensor.* entity in Home Assistant."""
    all_states = get_states()
    return [
        {
            "entity_id": s["entity_id"],
            "value": s["state"],
            "unit": s.get("attributes", {}).get("unit_of_measurement", ""),
        }
        for s in all_states
        if s["entity_id"].startswith("sensor.")
    ]