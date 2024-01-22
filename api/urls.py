from django.urls import path
from api.views import PokemonList

urlpatterns = [
    path('pokemons/', PokemonList.as_view(), name='pokemon-list'),
]