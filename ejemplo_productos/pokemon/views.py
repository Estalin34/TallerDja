from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from .models import Pokemon
from .forms import PokemonForm

def pokemon_create(request):
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pokemon_list")
    else:
        form = PokemonForm()
    return render(request, "pokemon_form.html", {"form": form})



def pokemon_list(request):
    search_query = request.GET.get('search', '')  
    pokemons = Pokemon.objects.all()  

    if search_query:
      
        pokemons = pokemons.filter(title__icontains=search_query)  
    page = int(request.GET.get("page", 1))  
    limit = 20  

    paginator = Paginator(pokemons, limit)
    page_obj = paginator.get_page(page)

    return render(request, "pokemon_list.html", {
        "page_obj": page_obj,
        "search": search_query  
    })

def pokemon_detail(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    return render(request, 'pokemon_detail.html', {'pokemon': pokemon})

def pokemon_edit(request, id):
    product = get_object_or_404(Pokemon, id=id)
    if request.method == "POST":
        form = PokemonForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("pokemon_list")
    else:
        form = PokemonForm(instance=product)
    return render(request, "pokemon_form.html", {"form": form})

def pokemon_delete(request, id):
    product = get_object_or_404(Pokemon, id=id)
    product.delete()
    return redirect("pokemon_list")


# views.py
from django.shortcuts import render
import requests

CUSTOM_API_URL = "https://api-322828854570.us-central1.run.app/"  # Ajusta esta URL si es necesario

def get_pokemon_cards():
    """ Obtiene las cartas de Pokémon de la API personalizada. """
    response = requests.get(CUSTOM_API_URL)
    if response.status_code == 200:
        return response.json().get('cards', [])  # Asegúrate de que estás obteniendo la lista de cartas
    return []

def pokemon_cards(request):
    """ Vista para mostrar las cartas de Pokémon. """
    cards = get_pokemon_cards()  # Obtiene las cartas de la API
    return render(request, 'pokemon_apis.html', {'cards': cards})

def pokemon_apis(request):
    return redirect("pokemon_apis")

