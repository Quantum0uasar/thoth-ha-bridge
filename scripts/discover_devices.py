#!/usr/bin/env python3
"""scripts/discover_devices.py – Print all HA entities grouped by domain.

Usage::

    python scripts/discover_devices.py
    python scripts/discover_devices.py --domain light sensor
"""
import argparse
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from ha_client.client import get_states, ping

DEFAULT_DOMAINS = [
    "light",
    "switch",
    "sensor",
    "binary_sensor",
    "climate",
    "media_player",
    "cover",
    "fan",
]


def discover(domains: list[str]) -> None:
    """Fetch all HA states and print entities grouped by domain."""
    if not ping():
        print("❌ Cannot reach Home Assistant.", file=sys.stderr)
        sys.exit(1)

    all_states = get_states()
    by_domain: dict[str, list[str]] = {d: [] for d in domains}

    for s in all_states:
        domain = s["entity_id"].split(".")[0]
        if domain in by_domain:
            by_domain[domain].append(s["entity_id"])

    total = 0
    for domain, entities in by_domain.items():
        if entities:
            print(f"\n── {domain.upper()} ({len(entities)}) ──")
            for e in sorted(entities):
                print(f"  {e}")
            total += len(entities)

    print(f"\nTotal: {total} entities across {len([d for d in by_domain if by_domain[d]])} domains.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Discover Home Assistant entities by domain.")
    parser.add_argument(
        "--domain",
        nargs="+",
        default=DEFAULT_DOMAINS,
        metavar="DOMAIN",
        help=f"Domains to list (default: {' '.join(DEFAULT_DOMAINS)})",
    )
    args = parser.parse_args()
    discover(args.domain)


if __name__ == "__main__":
    main()
