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

from django.shortcuts import render

def home(request):
    return render(request, "home.html")  # Asegúrate de que el archivo se llama home.html
