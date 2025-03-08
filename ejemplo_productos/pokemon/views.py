from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from .models import Pokemon

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

