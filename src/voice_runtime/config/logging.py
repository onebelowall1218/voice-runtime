import structlog
from structlog.processors import CallsiteParameterAdder, CallsiteParameter
from .settings import Settings



def configure_logging(settings: Settings):
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            CallsiteParameterAdder({
                CallsiteParameter.FILENAME, CallsiteParameter.LINENO, CallsiteParameter.FUNC_NAME
            }),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.add_log_level,
            structlog.processors.JSONRenderer(),
        ]
    )