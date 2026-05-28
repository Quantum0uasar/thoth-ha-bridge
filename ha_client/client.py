# ha_client/client.py – REST API wrapper
import requests
from config import HA_URL, HEADERS, REQUEST_TIMEOUT


def get_states() -> list:
    """Return all entity states from Home Assistant."""
    r = requests.get(f"{HA_URL}/api/states", headers=HEADERS, timeout=REQUEST_TIMEOUT)
    r.raise_for_status()
    return r.json()


def get_state(entity_id: str) -> dict:
    """Return the current state of a single entity."""
    r = requests.get(
        f"{HA_URL}/api/states/{entity_id}",
        headers=HEADERS,
        timeout=REQUEST_TIMEOUT,
    )
    r.raise_for_status()
    return r.json()


def call_service(domain: str, service: str, entity_id: str, **kwargs) -> dict:
    """Call any Home Assistant service.

    Args:
        domain:    HA service domain (e.g. ``light``, ``switch``).
        service:   Service name (e.g. ``turn_on``, ``turn_off``).
        entity_id: Target entity ID.
        **kwargs:  Extra service data forwarded in the request body.

    Returns:
        Parsed JSON response from Home Assistant.
    """
    payload = {"entity_id": entity_id, **kwargs}
    r = requests.post(
        f"{HA_URL}/api/services/{domain}/{service}",
        headers=HEADERS,
        json=payload,
        timeout=REQUEST_TIMEOUT,
    )
    r.raise_for_status()
    return r.json()


def ping() -> bool:
    """Return True if Home Assistant is reachable."""
    try:
        r = requests.get(f"{HA_URL}/api/", headers=HEADERS, timeout=REQUEST_TIMEOUT)
        return r.status_code == 200
    except requests.RequestException:
        return False
