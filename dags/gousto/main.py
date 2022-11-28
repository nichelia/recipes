from core import get_recipe
from pprint import pprint

def main(**kwargs):
    url = kwargs.get("url", None)
    data = get_recipe(url=url)
    
    if not data:
        raise ValueError('Recipe not found')

    return data.dict()

if __name__ == "__main__":
    pprint(main(**{"url":"https://www.gousto.co.uk/cookbook/chicken-recipes/broccoli-pesto-and-pangrattato-with-spinach-ricotta-ravioli"}))