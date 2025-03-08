import requests
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from ejemplo_productos.pokemon import models

API_URL = "https://pokeapi.co/api/v2/pokemon"
TOTAL_POKEMON = 1304  

def get_pokemon(id):
    """ Obtiene los datos detallados de un Pokémon y los devuelve en un diccionario. """
    response = requests.get(f"{API_URL}/{id}")
    if response.status_code == 200:
        pokemon_data = response.json()
        return {
            "id": id,
            "title": pokemon_data["name"].capitalize(),
            "image": pokemon_data["sprites"]["front_default"],
            "description": "Un Pokémon de la PokeAPI.",
            "type": [t["type"]["name"] for t in pokemon_data["types"]],
            "hp": pokemon_data["stats"][0]["base_stat"],
            "attack": pokemon_data["stats"][1]["base_stat"],
            "defense": pokemon_data["stats"][2]["base_stat"],
            "special_attack": pokemon_data["stats"][3]["base_stat"],
            "special_defense": pokemon_data["stats"][4]["base_stat"]
        }
    return None

def populate_pokemon():
    """ Recorre los Pokémon de la API y los guarda en la base de datos. """
    for i in range(1, TOTAL_POKEMON + 1):  
        pokemon_data = get_pokemon(i)
        if pokemon_data:
            pokemon, created = models.Pokemon.objects.get_or_create(
                title=pokemon_data["title"],
                defaults={
                    "description": pokemon_data["description"],
                    "type": pokemon_data["type"],
                    "image": pokemon_data["image"]
                }
            )
            if created:
                print(f" Guardado en BD: {pokemon.title}")
            else:
                print(f" Ya existe en BD: {pokemon.title}")

