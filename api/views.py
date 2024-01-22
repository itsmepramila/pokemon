from django.shortcuts import render
from rest_framework import generics
from api.seriallizers  import PokemonSerializer
from pokemons.models import Pokemon

# Create your views here.
class PokemonList(generics.ListAPIView):
    serializer_class=PokemonSerializer
    
    def get_queryset(self):
        queryset = Pokemon.objects.all()
        name = self.request.query_params.get('name', None)
        type_ = self.request.query_params.get('type', None)

        if name:
            queryset = queryset.filter(name__icontains=name)
        if type_:
            queryset = queryset.filter(type__icontains=type_)

        return queryset
