from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Genre, Game


def index(request):
    genres = Genre.objects.all()
    return render(request, 'games/index.html', {'latest_genres': genres})


def detail(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    return render(request, 'games/detail.html', {'genre': genre})


def favourite(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    try:
        game = genre.game_set.get(pk=request.POST['game'])
    except (KeyError, Game.DoesNotExist):
        return render(request, 'games/detail.html', {
            'genre': genre,
            'error_message': 'Incorrect game selected'
        })
    else:
        game.is_favourite = True
        game.save()
        return HttpResponseRedirect(reverse('game:detail', args=(genre.id,)))
