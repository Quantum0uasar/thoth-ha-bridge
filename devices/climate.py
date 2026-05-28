# devices/climate.py – Thermostat / HVAC controls
from __future__ import annotations
from typing import Literal, Optional
from ha_client.client import call_service, get_state

HvacMode = Literal["heat", "cool", "heat_cool", "auto", "off", "fan_only", "dry"]


def set_temperature(
    entity_id: str,
    temperature: float,
    target_temp_high: Optional[float] = None,
    target_temp_low: Optional[float] = None,
) -> dict:
    """Set the target temperature for a climate entity.

    Args:
        entity_id:        HA entity ID (e.g. ``climate.living_room``).
        temperature:      Single target temperature (used in heat/cool mode).
        target_temp_high: Upper bound for heat_cool / range mode.
        target_temp_low:  Lower bound for heat_cool / range mode.
    """
    kwargs: dict = {"temperature": temperature}
    if target_temp_high is not None:
        kwargs["target_temp_high"] = target_temp_high
    if target_temp_low is not None:
        kwargs["target_temp_low"] = target_temp_low
    return call_service("climate", "set_temperature", entity_id, **kwargs)


def set_hvac_mode(entity_id: str, mode: HvacMode) -> dict:
    """Set the HVAC operating mode.

    Args:
        entity_id: HA entity ID.
        mode:      One of ``heat``, ``cool``, ``heat_cool``, ``auto``,
                   ``off``, ``fan_only``, or ``dry``.
    """
    return call_service("climate", "set_hvac_mode", entity_id, hvac_mode=mode)


def set_fan_mode(entity_id: str, fan_mode: str) -> dict:
    """Set the fan mode (e.g. ``auto``, ``low``, ``high``)."""
    return call_service("climate", "set_fan_mode", entity_id, fan_mode=fan_mode)


def get_temperature(entity_id: str) -> dict:
    """Return current and target temperature info for a climate entity.

    Returns a dict with keys: ``current``, ``target``, ``mode``.
    """
    s = get_state(entity_id)
    attrs = s.get("attributes", {})
    return {
        "current": attrs.get("current_temperature"),
        "target": attrs.get("temperature"),
        "target_high": attrs.get("target_temp_high"),
        "target_low": attrs.get("target_temp_low"),
        "mode": s["state"],
        "fan_mode": attrs.get("fan_mode"),
    }
