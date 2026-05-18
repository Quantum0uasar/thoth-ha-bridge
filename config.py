import os
from dotenv import load_dotenv

load_dotenv()

HA_URL   = os.environ.get("HA_URL", "http://homeassistant.local:8123")
HA_TOKEN = os.environ.get("HA_TOKEN")

if not HA_TOKEN:
    raise ValueError("HA_TOKEN not set. Add it to your .env file.")

HA_WS_URL = HA_URL.replace("http", "ws") + "/api/websocket"

HEADERS = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json",
}