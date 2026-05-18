# ha_client/event_listener.py  –  Real-time state changes via WebSocket
import asyncio
import json
import websockets
from config import HA_WS_URL, HA_TOKEN


async def listen(on_event=None):
    if on_event is None:
        on_event = lambda e: print(
            f"[EVENT] {e['data']['entity_id']} → {e['data']['new_state']['state']}"
        )

    async with websockets.connect(HA_WS_URL) as ws:
        auth_req = json.loads(await ws.recv())
        assert auth_req["type"] == "auth_required"

        await ws.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
        auth_ok = json.loads(await ws.recv())
        assert auth_ok["type"] == "auth_ok", f"Auth failed: {auth_ok}"
        print("[WS] Authenticated with Home Assistant")

        await ws.send(json.dumps({
            "id": 1,
            "type": "subscribe_events",
            "event_type": "state_changed"
        }))
        print("[WS] Listening for state changes...\n")

        async for raw in ws:
            msg = json.loads(raw)
            if msg.get("type") == "event":
                on_event(msg["event"])


def start_listener(on_event=None):
    """Blocking helper – call this from normal (non-async) code."""
    asyncio.run(listen(on_event))