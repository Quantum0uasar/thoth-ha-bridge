# ha_client/client.py  –  REST API wrapper
import requests
from config import HA_URL, HEADERS


def get_states() -> list:
    """Return all entity states from Home Assistant."""
    r = requests.get(f"{HA_URL}/api/states", headers=HEADERS, timeout=10)
    r.raise_for_status()
    return r.json()


def get_state(entity_id: str) -> dict:
    """Return the current state of a single entity."""
    r = requests.get(f"{HA_URL}/api/states/{entity_id}", headers=HEADERS, timeout=10)
    r.raise_for_status()
    return r.json()


def call_service(domain: str, service: str, entity_id: str, **kwargs) -> dict:
    """Call any Home Assistant service."""
    payload = {"entity_id": entity_id, **kwargs}
    r = requests.post(
        f"{HA_URL}/api/services/{domain}/{service}",
        headers=HEADERS,
        json=payload,
        timeout=10,
    )
    r.raise_for_status()
    return r.json()


def ping() -> bool:
    """Return True if Home Assistant is reachable."""
    try:
        r = requests.get(f"{HA_URL}/api/", headers=HEADERS, timeout=5)
        return r.status_code == 200
    except requests.RequestException:
        return False