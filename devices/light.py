# devices/light.py  –  Light controls
from ha_client.client import call_service, get_state


def turn_on(entity_id: str, brightness: int = 255, color_temp: int = None):
    kwargs = {"brightness": brightness}
    if color_temp:
        kwargs["color_temp"] = color_temp
    return call_service("light", "turn_on", entity_id, **kwargs)


def turn_off(entity_id: str):
    return call_service("light", "turn_off", entity_id)


def toggle(entity_id: str):
    return call_service("light", "toggle", entity_id)


def set_rgb(entity_id: str, r: int, g: int, b: int):
    return call_service("light", "turn_on", entity_id, rgb_color=[r, g, b])


def get_brightness(entity_id: str):
    state = get_state(entity_id)
    return state.get("attributes", {}).get("brightness")