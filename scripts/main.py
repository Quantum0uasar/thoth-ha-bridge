# main.py  –  Entry point / demo
from ha_client.client import ping, get_states
from devices import light, sensor, switch


def main():
    print("Checking connection to Home Assistant...")
    if not ping():
        print("❌  Cannot reach Home Assistant. Check HA_URL and HA_TOKEN in config.py")
        return
    print("✅  Connected!\n")

    states = get_states()
    print(f"Found {len(states)} entities in Home Assistant.\n")

    # List all sensors
    sensors = [s for s in states if s["entity_id"].startswith("sensor.")]
    if sensors:
        s = sensors[0]
        print(f"Sample sensor: {s['entity_id']} = {s['state']}")

    # List all lights
    lights = [s["entity_id"] for s in states if s["entity_id"].startswith("light.")]
    print(f"\nLights found: {lights or 'none'}")

    # Uncomment to control devices:
    # light.turn_on("light.living_room", brightness=200)
    # switch.turn_on("switch.desk_fan")


if __name__ == "__main__":
    main()