from typing import List
import re
from markdownify import markdownify as md
from recipe_scrapers import scrape_me
from recipe_scrapers.goustojson import GoustoJson
import parse_ingredients

from app.gousto.schemas import Ingredient, Recipe, Query


def parse_ingredient_doses(raw_data: GoustoJson) -> List[str]:
    doses = []
    for ingredient in raw_data.get("ingredients", []):
        doses.append(ingredient.get("name", ""))
    for basic_ingredient in raw_data.get("basics", []):
        doses.append(basic_ingredient.get("title", ""))
    return doses


def parse_basic_ingredient(raw_data: GoustoJson) -> Ingredient:
    name = raw_data.get("title", "")
    allergens = []

    ingredient = Ingredient(
        name=name,
        allergens=allergens
    )
    return ingredient


def parse_ingredient(raw_data: GoustoJson) -> Ingredient:
    parse_name = parse_ingredients.parse_ingredient(raw_data.get("name", ""))
    name = parse_name.name if parse_name.name else parse_name.original_string
    image_url = ""
    if len(raw_data.get("media", {}).get("images", [])) > 0:
        image_url = raw_data["media"]["images"][0].get("image", "")
    allergens = []
    for allergen in raw_data.get("allergens", []).get("allergen", {}):
        allergens.append(allergen.get("slug"))
    
    ingredient = Ingredient(
        name=name,
        image_url=image_url,
        allergens=allergens
    )
    return ingredient


def parse_recipe(raw_data: GoustoJson, url:str) -> Recipe:
    name = raw_data.title()
    description = raw_data.data.get("description", "")
    cover_image_url = raw_data.image()
    recipe_rating = raw_data.data.get("rating", {}).get("average", 0)
    preperation_time_in_mins = raw_data.data.get("prep_times", {}).get("for_2", 0)
    cuisine = raw_data.data.get("cuisine", {}).get("title", "")
    ingredients = [parse_ingredient(data) for data in raw_data.data.get("ingredients", [])]
    ingredients.extend([parse_basic_ingredient(data) for data in raw_data.data.get("basics", [])])
    ingredient_doses = parse_ingredient_doses(raw_data.data)
    instructions = []
    allergens = [allergen.get("title", "") for allergen in raw_data.data.get("allergens", [])]
    nutritional_information_per_grams = [] # TODO
    nutritional_information_per_portion = [] # TODO

    for cooking_instruction in raw_data.data.get("cooking_instructions", []):
        instruction = md(cooking_instruction.get("instruction", ""))
        if len(cooking_instruction.get("media", {}).get("images", [])) > 0:
            instructions.append(f'{cooking_instruction["media"]["images"][0].get("image", "")} {instruction}')
        else:
            instructions.append(instruction)

    recipe = Recipe(
        name=name,
        description=description,
        cover_image_url=cover_image_url,
        url=url,
        recipe_rating=recipe_rating,
        preperation_time_in_mins=preperation_time_in_mins,
        cuisine=cuisine,
        ingredients=ingredients,
        ingredient_doses=ingredient_doses,
        instructions=instructions,
        allergens=allergens,
        nutritional_information_per_grams=nutritional_information_per_grams,
        nutritional_information_per_portion=nutritional_information_per_portion
    )
    return recipe


def get_recipe(url: str) -> Recipe:
    if not url:
        raise ValueError('Url of gousto recipe not provided') 
    
    scraper = scrape_me(url)
    recipe = parse_recipe(scraper, url)
    return recipe