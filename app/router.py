from fastapi import APIRouter

from app.gousto import api as gousto_api

api_router = APIRouter()

api_router.include_router(gousto_api.router, prefix="/gousto", tags=["Recipes"])