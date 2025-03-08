# Importaciones necesarias
import requests
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from ejemplo_productos.pokemon import models



# Constantes
API_URL = "https://pokeapi.co/api/v2/pokemon"
TOTAL_POKEMON = 1304  # Total de Pokémon en la API

# Modelo Pokémon
class Pokemon(models.Model):
    title = models.CharField(max_length=100, unique=True)  # Agregamos unique para evitar duplicados
    description = models.TextField()
    type = models.JSONField()
    image = models.URLField()

    def __str__(self):
        return self.title


# Función para obtener Pokémon de la API
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
        }
    return None


# Función para poblar la base de datos con Pokémon
def populate_pokemon():
    """ Recorre los Pokémon de la API y los guarda en la base de datos. """
    for i in range(1, TOTAL_POKEMON + 1):  
        pokemon_data = get_pokemon(i)
        if pokemon_data:
            pokemon, created = Pokemon.objects.get_or_create(
                title=pokemon_data["title"],
                defaults={
                    "description": pokemon_data["description"],
                    "type": pokemon_data["type"],
                    "image": pokemon_data["image"]
                }
            )
            if created:
                print(f"✅ Guardado en BD: {pokemon.title}")
            else:
                print(f"⚠️ Ya existe en BD: {pokemon.title}")


# Vista para listar Pokémon con paginación
def pokemon_list(request):
    page = int(request.GET.get("page", 1))  # Obtiene la página actual, por defecto 1
    limit = 20  # Pokémon por página

    pokemons = Pokemon.objects.all()  
    paginator = Paginator(pokemons, limit)
    page_obj = paginator.get_page(page)

    return render(request, "pokemon_list.html", {
        "page_obj": page_obj,
    })


# Vista para ver detalles de un Pokémon
def pokemon_detail(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    return render(request, "pokemon_detail.html", {"pokemon": pokemon})
