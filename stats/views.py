
from django.views import generic
from .models import Player




class IndexView(generic.ListView):
    template_name = 'stats/index.html'

    def get_queryset(self):
        return Player.objects.all()



