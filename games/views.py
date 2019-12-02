from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Genre, Game


class IndexView(generic.ListView):
    context_object_name = 'latest_genres'
    template_name = 'games/index.html'

    def get_queryset(self):
        return Genre.objects.all()


class DetailView(generic.DetailView):
    model = Genre
    template_name = 'games/detail.html'


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
        game.is_favorite = True
        game.save()
        return HttpResponseRedirect(reverse('game:detail', args=(genre.id,)))
