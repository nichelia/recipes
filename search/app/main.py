from fastapi import Depends, FastAPI, status

from app import config
from app.router import api_router
from app.logger import get_logger
from app.queue import init_queue_pool

logger = get_logger(__name__)
global_settings = config.Settings()


app = FastAPI(title=global_settings.project_name,
              openapi_url=f"{global_settings.api_v1_prefix}/openapi.json",
              version=global_settings.version,
              debug=global_settings.debug)

app.include_router(api_router, prefix=global_settings.api_v1_prefix)


@app.on_event("startup")
async def startup_event():
    logger.info("Search service loading...")
    app.state.queue = await init_queue_pool()


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Search service unloading...")
    await app.state.queue.close()


@app.get("/", tags=["App Info"])
async def app_info(settings: config.Settings = Depends(config.get_settings)):
    app.state.queue.xadd("Hello World", {"hello": "world"}, '*')
    return {"name": settings.project_name,
            "description": "[todo]",
            "documentation": "/docs",
            "version": settings.version}


@app.get("/health", tags=["Health check"])
async def health_check(settings: config.Settings = Depends(config.get_settings)):
    try:
        await app.state.queue.set(str(settings.queue_url), settings.running)
        queue_status = await app.state.queue.get(str(settings.queue_url))
    except Exception:  # noqa: E722
        logger.exception("Sorry no power we can't open bakery...")
        queue_status = settings.not_running
    return {
        "Web server": settings.running,
        "Queue": queue_status
    }