from fastapi import FastAPI, status

from app import config
from app.router import api_router
from redis_om import get_redis_connection


app = FastAPI(title=config.PROJECT_NAME,
              openapi_url=f"{config.API_V1_PREFIX}/openapi.json",
              version=config.VERSION,
              debug=config.DEBUG)

app.include_router(api_router, prefix=config.API_V1_PREFIX)

redis = get_redis_connection(
    host="queue",
    port=6379,
    password="",
    decode_responses=True
)

@app.get("/", tags=["Health check"])
@app.get('/health', tags=["Health check"])
async def health_check():
    return {"name": config.PROJECT_NAME,
            "description": "[todo]",
            "documentation": "/docs",
            "version": config.VERSION}