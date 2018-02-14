from django.db import models
from django.core.urlresolvers import reverse
class Team(models.Model):
    team_name = models.CharField(max_length=200)
    team_logo = models.FileField()
    city = models.CharField(max_length=200)
    city_image = models.FileField()
    arena = models.CharField(max_length=200)
    arena_image = models.FileField()

    def get_absolute_url(self):
        return reverse('roster:detail', kwargs={'pk' : self.pk})

    def __str__(self):
        return self.team_name


class Person(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    person_number = models.CharField(max_length=3)
    person_name = models.CharField(max_length=200)
    person_position = models.CharField(max_length=50)
    person_image = models.FileField()
    person_age = models.CharField(max_length=2)

    def __str__(self):
        return self.person_name
