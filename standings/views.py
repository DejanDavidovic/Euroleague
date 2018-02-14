from django.views import generic
from .models import Table




class IndexView(generic.ListView):
    template_name = 'standings/index.html'

    def get_queryset(self):
        return Table.objects.all()

