from fastapi import FastAPI, status

from app import config
from app.router import api_router


app = FastAPI(title=config.PROJECT_NAME,
              openapi_url=f"{config.API_V1_PREFIX}/openapi.json",
              version=config.VERSION,
              debug=config.DEBUG)

app.include_router(api_router, prefix=config.API_V1_PREFIX)

@app.get("/", tags=["Health check"])
@app.get('/health', tags=["Health check"])
async def health_check():
    return {"name": config.PROJECT_NAME,
            "description": "[todo]",
            "documentation": "/docs",
            "version": config.VERSION}