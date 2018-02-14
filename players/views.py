from django.views import generic
from .models import Player
from django.views.generic.edit import CreateView,DeleteView
from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):

    template_name = 'players/index.html'

    def get_queryset(self):
        return Player.objects.all()


class DetailView(generic.DetailView):
    model = Player
    template_name = 'players/detail.html'

class AddPlayer(CreateView) :
    model = Player
    fields = ['player_name','player_face','player_position','player_nationality','date_of_birth','player_team','player_height']

class DeletePlayer(DeleteView):
    model = Player
    success_url = reverse_lazy('players:index')



