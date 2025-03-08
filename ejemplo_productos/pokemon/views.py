from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from .models import Pokemon


def pokemon_list(request):
    page = int(request.GET.get("page", 1))  # Obtiene la página actual, por defecto 1
    limit = 20  # Pokémon por página

    pokemons = Pokemon.objects.all()  # Obtiene todos los Pokémon de la base de datos
    paginator = Paginator(pokemons, limit)
    page_obj = paginator.get_page(page)

    return render(request, "pokemon_list.html", {
        "page_obj": page_obj,
    })



def pokemon_detail(request, id):  # El parámetro debe llamarse "id"
    pokemon = get_object_or_404(Pokemon, id=id)
    return render(request, 'pokemon_detail.html', {'pokemon': pokemon})

