from django.urls import path

from . import views

urlpatterns = [
    # ex: /games/
    path('', views.index, name='index'),
    # ex: /games/5/details
    path('<int:genre_id>/details', views.detail, name='detail'),
]