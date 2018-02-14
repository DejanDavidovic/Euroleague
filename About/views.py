from django.views import generic
from .models import asdsa

class IndexView(generic.ListView):
    template_name = 'About/index.html'

    def get_queryset(self):
        return asdsa.objects.all()