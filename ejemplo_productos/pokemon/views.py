from django.shortcuts import render, get_object_or_404
from .services.pokemon_service import get_pokemons
from django.core.paginator import Paginator

from .models import Pokemon

from django.shortcuts import render
from .services.pokemon_service import get_pokemons

from django.core.paginator import Paginator
from django.shortcuts import render
from .services.pokemon_service import get_pokemons
from django.shortcuts import render
from .services.pokemon_service import get_pokemons

def pokemon_list(request):
    page = int(request.GET.get("page", 1))  # Obtiene la página actual, por defecto 1
    limit = 20  # Pokémon por página

    data = get_pokemons(page, limit)
    pokemons = data["pokemons"]
    total_pokemons = data["total"]
    total_pages = (total_pokemons // limit) + (1 if total_pokemons % limit else 0)

    return render(request, "pokemon_list.html", {
        "page_obj": pokemons,
        "page_number": page,
        "total_pages": total_pages,
    })



def pokemon_detail(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    return render(request, "pokemon_detail.html", {"pokemon": pokemon})
