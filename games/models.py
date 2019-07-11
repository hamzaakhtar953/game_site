from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=200)
    total_games = models.FloatField(default=0)

    def __str__(self):
        return f'{self.title}. Total Games: {self.total_games}'


class Game(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    developer_name = models.CharField(max_length=200)
    game_logo = models.CharField(max_length=1000)
    game_size = models.FloatField(default=0)

    def __str__(self):
        return f'{self.title} created by developer {self.developer_name}'
