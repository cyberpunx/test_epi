from django.shortcuts import render
from rest_framework import viewsets
from .models import Game
from .serializer import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer