import json
import re

import structlog

from voice_runtime.config.logging import configure_logging
from voice_runtime.config.settings import Settings


def test_console_format_for_local_env(capsys):
    configure_logging(Settings(app_env="local", log_level="INFO"))
    log = structlog.get_logger()

    log.info("hello world")

    out = capsys.readouterr().out.strip()
    pattern = (
        r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z?: "
        r".*test_logging\.py: test_logging: "
        r"test_console_format_for_local_env: \d+: \[INFO\] hello world$"
    )
    assert re.match(pattern, out), out


def test_json_format_for_non_local_env(capsys):
    configure_logging(Settings(app_env="production", log_level="INFO"))
    log = structlog.get_logger()

    log.info("hello world", turn_id="abc123")

    out = capsys.readouterr().out.strip()
    payload = json.loads(out)

    assert payload["event"] == "hello world"
    assert payload["level"] == "info"
    assert payload["func_name"] == "test_json_format_for_non_local_env"
    assert payload["module"] == "test_logging"
    assert payload["turn_id"] == "abc123"
