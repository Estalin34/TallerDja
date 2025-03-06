import requests
from pokemon.models import Pokemon
import requests

API_URL = "https://pokeapi.co/api/v2/pokemon"

def get_pokemons(page=1, limit=20):
    """ Obtiene una lista de Pokémon desde la API con paginación """
    offset = (page - 1) * limit  # Calculamos el offset
    response = requests.get(f"{API_URL}?offset={offset}&limit={limit}")

    if response.status_code == 200:
        data = response.json()
        pokemons = []
        for pokemon in data["results"]:
            pokemon_id = pokemon["url"].split("/")[-2]  # Extrae el ID del URL
            pokemon_data = get_pokemon(pokemon_id)
            pokemons.append(pokemon_data)

        return {
            "pokemons": pokemons,
            "total": data["count"],  # Total de Pokémon en la API
        }
    return {"pokemons": [], "total": 0}

def get_pokemon(id):
    """ Obtiene los datos detallados de un Pokémon """
    response = requests.get(f"{API_URL}/{id}")
    if response.status_code == 200:
        pokemon_data = response.json()
        return {
            "id": id,
            "title": pokemon_data["name"].capitalize(),
            "image": pokemon_data["sprites"]["front_default"],
            "description": "Un Pokémon de la PokeAPI.",
            "type": [t["type"]["name"] for t in pokemon_data["types"]],
        }
    return {}
