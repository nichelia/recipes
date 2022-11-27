import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

from app.logger import get_logger

logger = get_logger(__name__)


class Settings(BaseSettings):
    debug: str = os.getenv("DEBUG", "1")
    testing: str = os.getenv("TESTING", "0")
    api_v1_prefix: str = os.getenv("API_V1_PREFIX", "/api/v1")
    project_name: str = os.getenv("PROJECT_NAME", "search")
    version: str = os.getenv("VERSION", "0.0.0")
    queue_url: AnyUrl = os.environ.get("QUEUE_URL", "redis://queue")
    queue_password: str = os.getenv("QUEUE_PASSWORD", "")
    queue_db: int = int(os.getenv("QUEUE_DB", "0"))
    running: str = "up"
    not_running: str = "down"
    web_server: str = "Web Server"


@lru_cache()
def get_settings() -> BaseSettings:
    logger.info("Loading config settings from the environment...")
    return Settings()