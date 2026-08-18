import structlog
from structlog.processors import CallsiteParameterAdder, CallsiteParameter
from structlog.typing import EventDict, WrappedLogger

from .settings import Settings


def _console_renderer(_logger: WrappedLogger, _method_name: str, event_dict: EventDict) -> str:
    timestamp = event_dict.pop("timestamp", "")
    pathname = event_dict.pop("pathname", "")
    module = event_dict.pop("module", "")
    func_name = event_dict.pop("func_name", "")
    lineno = event_dict.pop("lineno", "")
    level = event_dict.pop("level", "").upper()
    message = event_dict.pop("event", "")

    line = f"{timestamp}: {pathname}: {module}: {func_name}: {lineno}: [{level}] {message}"

    extras = " ".join(f"{key}={value!r}" for key, value in event_dict.items())
    return f"{line} {extras}" if extras else line


def configure_logging(settings: Settings) -> None:
    renderer = (
        _console_renderer
        if settings.app_env == "local"
        else structlog.processors.JSONRenderer()
    )

    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            CallsiteParameterAdder({
                CallsiteParameter.PATHNAME,
                CallsiteParameter.MODULE,
                CallsiteParameter.FUNC_NAME,
                CallsiteParameter.LINENO,
            }),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.add_log_level,
            renderer,
        ]
    )