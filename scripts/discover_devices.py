# scripts/discover_devices.py  –  Print all HA entities by domain
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from ha_client.client import get_states

DOMAINS = ["light", "switch", "sensor", "binary_sensor", "climate", "media_player"]

def main():
    all_states = get_states()
    by_domain = {d: [] for d in DOMAINS}

    for s in all_states:
        domain = s["entity_id"].split(".")[0]
        if domain in by_domain:
            by_domain[domain].append(s["entity_id"])

    for domain, entities in by_domain.items():
        if entities:
            print(f"\n── {domain.upper()} ({len(entities)}) ──")
            for e in entities:
                print(f"   {e}")

if __name__ == "__main__":
    main()