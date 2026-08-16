#!/usr/bin/env bash
set -euo pipefail

source env/bin/activate
exec python -m uvicorn voice_runtime.api.app:create_app --factory --reload