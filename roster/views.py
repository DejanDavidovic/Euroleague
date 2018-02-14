from django.views import generic
from .models import Team,Person


class IndexView(generic.ListView):
    template_name = 'roster/index.html'

    def get_queryset(self):
        return Team.objects.all()


class DetailView(generic.DetailView):
    model = Team
    template_name = 'roster/detail.html'

