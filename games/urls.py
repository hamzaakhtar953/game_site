from django.urls import path

from . import views

app_name = 'game'

urlpatterns = [
    # ex: /games/
    path('', views.index, name='index'),
    # ex: /games/5/details
    path('<int:genre_id>/details', views.detail, name='detail'),
    # ex: /games/5/favourite    
    path('<int:genre_id>/favourite', views.favourite, name='favourite'),
]
