
from django.db import models
from django.core.urlresolvers import reverse
class Player(models.Model):
    player_name = models.CharField(max_length=200)
    player_face = models.FileField()
    player_position = models.CharField(max_length=200)
    player_nationality = models.CharField(max_length=200)
    date_of_birth = models.CharField(max_length=200)
    player_team = models.CharField(max_length=200)
    player_height = models.CharField(max_length=200)



    def get_absolute_url(self):
        return reverse('players:detail', kwargs={'pk' : self.pk})

    def __str__(self):
        return self.player_name


class Stat(models.Model):
    stats = models.ForeignKey(Player, on_delete=models.CASCADE)
    games_played = models.DecimalField(decimal_places=0, max_digits=2)
    games_started = models.DecimalField(decimal_places=0, max_digits=2)
    minutes = models.CharField(max_length=200)
    points = models.DecimalField(decimal_places=1, max_digits=6)
    two_point = models.CharField(max_length=200)
    three_point = models.CharField(max_length=200)
    free_throw = models.CharField(max_length=200)
    rebounds = models.DecimalField(decimal_places=1, max_digits=6)
    assists =  models.DecimalField(decimal_places=1, max_digits=6)
    steals = models.DecimalField(decimal_places=1, max_digits=6)
    turnovers = models.DecimalField(decimal_places=1, max_digits=6)
    blocks = models.DecimalField(decimal_places=1, max_digits=6)
    index = models.DecimalField(decimal_places=1, max_digits=6)

    def __str__(self):
        return self.minutes






