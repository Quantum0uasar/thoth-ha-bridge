# thoth-ha-bridge

A Python bridge that connects **Home Assistant** to smart home devices — part of the [Thothcraft](https://www.thothcraft.com) ecosystem.

The Thoth app runs ML models on your device (Mac, Windows, Raspberry Pi) and detects things like occupancy, activity, and sleep state. This bridge takes those predictions from Home Assistant and uses them to control your physical smart home devices.

## How It Works

```
Thoth Dashboard (localhost:8000)
        │
        ▼
  Home Assistant          ← receives ML predictions as native sensors
        │
        ▼
  thoth-ha-bridge         ← this repo
        │
        ▼
  Smart Devices           ← lights, switches, thermostat, sensors
```

## Project Structure

```
thoth-ha-bridge/
├── config.py                  # HA URL + token config
├── main.py                    # Entry point / demo
├── requirements.txt
├── ha_client/
│   ├── client.py              # REST API wrapper (get states, call services, ping)
│   └── event_listener.py      # WebSocket listener for real-time state changes
├── devices/
│   ├── light.py               # Turn on/off, brightness, RGB
│   ├── switch.py              # Toggle smart plugs and switches
│   ├── sensor.py              # Read temperature, humidity, motion
│   └── climate.py             # Thermostat and HVAC control
└── scripts/
    └── discover_devices.py    # Lists all HA entities grouped by domain
```

## Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Home Assistant

Edit `config.py` with your Home Assistant URL and a Long-Lived Access Token:

```python
HA_URL   = "http://homeassistant.local:8123"
HA_TOKEN = "your_token_here"
```

To get a token: **HA → Profile (bottom-left) → Long-Lived Access Tokens → Create Token**

### 3. Discover your devices

```bash
python scripts/discover_devices.py
```

### 4. Run the bridge

```bash
python main.py
```

## Device Modules

| Module | What it controls |
|---|---|
| `devices/light.py` | Lights — on/off, brightness, RGB color |
| `devices/switch.py` | Smart plugs and switches |
| `devices/sensor.py` | Read sensor values (temp, humidity, motion) |
| `devices/climate.py` | Thermostat — temperature and HVAC mode |

## Requirements

- Python 3.8+
- Home Assistant instance (local or remote)
- Long-Lived Access Token from HA

## Related

- [Thothcraft](https://www.thothcraft.com) — the main platform
- [Thoth GitHub](https://github.com/Thothcraft/thoth) — edge sensor app
- [Research Portal](https://portal-three-rho.vercel.app) — model training and deployment

## License

MIT
