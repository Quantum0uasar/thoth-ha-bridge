import os
from dotenv import load_dotenv

load_dotenv()

# Home Assistant connection settings
HA_URL    = os.environ.get("HA_URL", "http://homeassistant.local:8123")
HA_TOKEN  = os.environ.get("HA_TOKEN")

if not HA_TOKEN:
    raise ValueError("HA_TOKEN not set. Add it to your .env file.")

# Derive WebSocket URL from REST URL
HA_WS_URL = HA_URL.replace("http", "ws") + "/api/websocket"

# HTTP request timeout in seconds
REQUEST_TIMEOUT = int(os.environ.get("REQUEST_TIMEOUT", "10"))

# WebSocket reconnect settings
WS_RECONNECT_DELAY   = float(os.environ.get("WS_RECONNECT_DELAY", "5.0"))   # seconds
WS_MAX_RECONNECTS    = int(os.environ.get("WS_MAX_RECONNECTS", "10"))

HEADERS = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json",
}
