#!/usr/bin/env python3
"""scripts/main.py – Entry point / demo for thoth-ha-bridge.

Usage::

    python scripts/main.py           # run status check
    python scripts/main.py --listen  # status check + stream events
"""
import argparse
import logging
import sys

from ha_client.client import ping, get_states
from ha_client.event_listener import start_listener

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def run_status_check() -> bool:
    """Print a summary of the current HA state.  Returns True on success."""
    print("Checking connection to Home Assistant...")
    if not ping():
        print("❌ Cannot reach Home Assistant. Check HA_URL and HA_TOKEN in your .env file.")
        return False
    print("✅ Connected!\n")

    states = get_states()
    print(f"Found {len(states)} entities in Home Assistant.\n")

    # Sensors
    sensors = [s for s in states if s["entity_id"].startswith("sensor.")]
    if sensors:
        s = sensors[0]
        print(f"Sample sensor : {s['entity_id']} = {s['state']}")

    # Lights
    lights = [s["entity_id"] for s in states if s["entity_id"].startswith("light.")]
    print(f"Lights found  : {', '.join(lights) if lights else 'none'}")

    # Switches
    switches = [s["entity_id"] for s in states if s["entity_id"].startswith("switch.")]
    print(f"Switches found: {', '.join(switches) if switches else 'none'}\n")

    return True


def main():
    parser = argparse.ArgumentParser(description="thoth-ha-bridge demo")
    parser.add_argument(
        "--listen",
        action="store_true",
        help="After status check, stream state_changed events from Home Assistant.",
    )
    args = parser.parse_args()

    ok = run_status_check()
    if not ok:
        sys.exit(1)

    if args.listen:
        print("Starting event listener (Ctrl+C to stop)...\n")
        start_listener()


if __name__ == "__main__":
    main()
