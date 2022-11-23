from typing import List, Optional, Union

from pydantic import BaseModel, HttpUrl


class Ingredient(BaseModel):
    name: str
    image_url: Optional[Union[HttpUrl, str]] = ""
    allergens: List[str]


class Recipe(BaseModel):
    name: str
    description: str
    cover_image_url: HttpUrl
    url: HttpUrl
    gousto_rating: int
    preperation_time_in_mins: int
    cuisine: str
    ingredients: List[Ingredient]
    ingredient_doses: List[str]
    instructions: List[str]
    allergens: List[str]
    nutritional_information_per_grams: List[str]
    nutritional_information_per_portion: List[str]


class GoustoQuery(BaseModel):
    url: str = ""


class GoustoResponse(BaseModel):
    status: bool = True
    message: str = "Success"
    data: Recipe