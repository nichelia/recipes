from fastapi import APIRouter

from app.gousto.core import get_recipe
from app.gousto.schemas import Query, Response
from app import main

router = APIRouter()


@router.post("/search/", response_model=Response)
def search(data: Query):
    data = get_recipe(data=data)
    status, message = (True, "Success") if data else (False, "Recipe not found!")
    ret = Response(status=status, message=message, data=data)
    # main.app.state.queue.xadd('search_completed', ret.dict(), '*')

    return ret