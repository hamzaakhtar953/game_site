from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Genre


def index(request):
    genres = Genre.objects.all()
    return render(request, 'games/index.html', {'latest_genres': genres})


def detail(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    return render(request, 'games/detail.html', {'genre': genre})
