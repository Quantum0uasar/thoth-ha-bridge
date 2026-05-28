# devices/sensor.py – Read sensor values
from __future__ import annotations
from typing import Optional, Union
from ha_client.client import get_state, get_states


def read(entity_id: str) -> dict:
    """Return state + attributes for any sensor entity.

    Returns a dict with keys: ``entity_id``, ``value``, ``unit``, ``last_updated``.
    """
    s = get_state(entity_id)
    return {
        "entity_id": s["entity_id"],
        "value": s["state"],
        "unit": s.get("attributes", {}).get("unit_of_measurement", ""),
        "last_updated": s.get("last_updated"),
    }


def get_numeric_value(entity_id: str) -> Optional[float]:
    """Return the sensor state as a float, or None if it cannot be parsed.

    Useful for ML feature pipelines that need numeric sensor readings.
    """
    s = get_state(entity_id)
    try:
        return float(s["state"])
    except (ValueError, TypeError):
        return None


def get_all_sensors() -> list[dict]:
    """Return a summary of every ``sensor.*`` entity in Home Assistant."""
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
