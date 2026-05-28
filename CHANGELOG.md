# Changelog

All notable changes to **thoth-ha-bridge** are documented here.
This project follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and [Semantic Versioning](https://semver.org/).

---

## [Unreleased]

### Added
- `config.py`: `REQUEST_TIMEOUT`, `WS_RECONNECT_DELAY`, and `WS_MAX_RECONNECTS` environment-variable overrides.
- `devices/light.py`: `set_effect()` helper; `transition` parameter on `turn_on()` / `turn_off()`.
- `devices/sensor.py`: `get_numeric_value()` helper for ML feature pipelines.
- `devices/switch.py`: `set_state(entity_id, on=bool)` convenience helper.
- `ha_client/event_listener.py`: Automatic WebSocket reconnect loop with configurable delay and max-attempt cap.
- `scripts/main.py`: `--listen` CLI flag, `argparse` integration, switch summary, and proper logging setup.

### Changed
- `ha_client/client.py`: All request timeouts now read from `REQUEST_TIMEOUT` config instead of a hardcoded `10` s value.
- `ha_client/event_listener.py`: `print()` calls replaced with `logging` for structured output.
- All device modules: Full PEP 484 type annotations and Google-style docstrings added.

---

## [0.1.0] – 2026-05-21

### Added
- Initial project scaffold: `ha_client/`, `devices/`, `scripts/`.
- REST API wrapper (`client.py`) with `get_states`, `get_state`, `call_service`, and `ping`.
- WebSocket event listener (`event_listener.py`) for real-time `state_changed` events.
- Device helpers: `light.py`, `sensor.py`, `switch.py`, `climate.py`.
- Environment-variable configuration via `.env` (using `python-dotenv`).
- MIT License.
