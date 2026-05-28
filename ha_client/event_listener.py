# ha_client/event_listener.py – Real-time state changes via WebSocket
import asyncio
import json
import logging
import websockets
from config import HA_WS_URL, HA_TOKEN, WS_RECONNECT_DELAY, WS_MAX_RECONNECTS

logger = logging.getLogger(__name__)


async def listen(on_event=None):
    """Connect to Home Assistant WebSocket and stream state_changed events.

    Automatically reconnects on connection failure up to *WS_MAX_RECONNECTS* times
    with a *WS_RECONNECT_DELAY* second pause between attempts.

    Args:
        on_event: Optional callback ``(event: dict) -> None``.  Defaults to
            printing the entity_id and new state to stdout.
    """
    if on_event is None:
        def on_event(e):
            entity = e.get("data", {}).get("entity_id", "unknown")
            new_state = e.get("data", {}).get("new_state", {}).get("state", "?")
            print(f"[EVENT] {entity} → {new_state}")

    attempt = 0
    while True:
        try:
            async with websockets.connect(HA_WS_URL) as ws:
                attempt = 0  # reset on successful connection
                auth_req = json.loads(await ws.recv())
                assert auth_req["type"] == "auth_required"

                await ws.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
                auth_ok = json.loads(await ws.recv())
                assert auth_ok["type"] == "auth_ok", f"Auth failed: {auth_ok}"
                logger.info("[WS] Authenticated with Home Assistant")

                await ws.send(json.dumps({
                    "id": 1,
                    "type": "subscribe_events",
                    "event_type": "state_changed",
                }))
                logger.info("[WS] Listening for state changes...")

                async for raw in ws:
                    msg = json.loads(raw)
                    if msg.get("type") == "event":
                        on_event(msg["event"])

        except (websockets.ConnectionClosed, OSError) as exc:
            attempt += 1
            if attempt > WS_MAX_RECONNECTS:
                logger.error("[WS] Max reconnect attempts reached. Giving up.")
                raise
            logger.warning(
                "[WS] Connection lost (%s). Reconnecting in %.1fs (attempt %d/%d)...",
                exc, WS_RECONNECT_DELAY, attempt, WS_MAX_RECONNECTS,
            )
            await asyncio.sleep(WS_RECONNECT_DELAY)


def start_listener(on_event=None):
    """Blocking helper – call this from normal (non-async) code."""
    asyncio.run(listen(on_event))
