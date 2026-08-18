from fastapi import FastAPI

from voice_runtime.api.routes.health import router as health_router
from voice_runtime.config.logging import configure_logging
from voice_runtime.config.settings import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    configure_logging(settings)

    app = FastAPI()
    app.include_router(health_router)
    return app
