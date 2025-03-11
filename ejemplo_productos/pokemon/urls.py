from django.urls import path
from .views import pokemon_list, pokemon_detail,pokemon_create,pokemon_edit,pokemon_delete

urlpatterns = [
    path('', pokemon_list, name='pokemon_list'),
    path('<int:id>/', pokemon_detail, name='pokemon_detail'), 
    path('create/', pokemon_create, name='pokemon_create'),
    path('edit/<int:id>/', pokemon_edit, name='pokemon_edit'),
    path('delete/<int:id>/', pokemon_delete, name='pokemon_delete'),
]
