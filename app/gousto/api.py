from fastapi import APIRouter

from app.gousto.core import get_recipe
from app.gousto.schemas import GoustoQuery, GoustoResponse

router = APIRouter()


@router.post("/search/", response_model=GoustoResponse)
def search(data: GoustoQuery):
    data = get_recipe(data=data)
    status, message = (True, "Success") if data else (False, "Recipe not found!")

    return GoustoResponse(status=status, message=message, data=data)