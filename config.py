# config.py  –  Home Assistant connection config

# How to get your token:
#   HA → Profile (bottom-left) → Long-Lived Access Tokens → Create Token

HA_URL   = "http://homeassistant.local:8123"
HA_TOKEN = "YOUR_LONG_LIVED_TOKEN_HERE"

HA_WS_URL = HA_URL.replace("http", "ws") + "/api/websocket"

HEADERS = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json",
}