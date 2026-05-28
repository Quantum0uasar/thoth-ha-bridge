# devices/light.py – Light controls
from __future__ import annotations
from typing import Optional
from ha_client.client import call_service, get_state


def turn_on(
    entity_id: str,
    brightness: int = 255,
    color_temp: Optional[int] = None,
    transition: Optional[float] = None,
) -> dict:
    """Turn on a light entity.

    Args:
        entity_id:  HA entity ID (e.g. ``light.living_room``).
        brightness: 0–255 brightness level. Defaults to 255 (full).
        color_temp: Mireds color temperature, or ``None`` to leave unchanged.
        transition: Transition time in seconds, or ``None`` for instant.
    """
    kwargs: dict = {"brightness": brightness}
    if color_temp is not None:
        kwargs["color_temp"] = color_temp
    if transition is not None:
        kwargs["transition"] = transition
    return call_service("light", "turn_on", entity_id, **kwargs)


def turn_off(entity_id: str, transition: Optional[float] = None) -> dict:
    """Turn off a light entity.

    Args:
        entity_id:  HA entity ID.
        transition: Transition time in seconds, or ``None`` for instant.
    """
    kwargs: dict = {}
    if transition is not None:
        kwargs["transition"] = transition
    return call_service("light", "turn_off", entity_id, **kwargs)


def toggle(entity_id: str) -> dict:
    """Toggle a light entity between on and off."""
    return call_service("light", "toggle", entity_id)


def set_rgb(entity_id: str, r: int, g: int, b: int) -> dict:
    """Set a light to a specific RGB colour.

    Args:
        entity_id: HA entity ID.
        r, g, b:   Red / Green / Blue components in range 0–255.
    """
    return call_service("light", "turn_on", entity_id, rgb_color=[r, g, b])


def set_effect(entity_id: str, effect: str) -> dict:
    """Apply a named light effect (e.g. ``"Rainbow"``).\n\n    The available effects depend on the integration powering the light.
    """
    return call_service("light", "turn_on", entity_id, effect=effect)


def get_brightness(entity_id: str) -> Optional[int]:
    """Return the current brightness (0–255) of a light, or None if unavailable."""
    state = get_state(entity_id)
    return state.get("attributes", {}).get("brightness")
