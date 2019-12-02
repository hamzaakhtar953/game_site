from django.urls import path

from . import views

app_name = 'game'

urlpatterns = [
    # ex: /games/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /games/5/details
    path('<int:pk>/details', views.DetailView.as_view(), name='detail'),
    # ex: /games/5/favourite
    path('<int:genre_id>/favourite', views.favourite, name='favourite'),
]
