from django.views import generic
from .models import video_type,video
from django.views.generic.edit import CreateView,DeleteView
from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'videos/index.html'

    def get_queryset(self):
        return video_type.objects.all()


class DetailView(generic.DetailView):
    model = video_type
    template_name = 'videos/detail.html'

class AddVideo(CreateView):
    model = video
    fields = ['type', 'name', 'file']

class DeleteVideo(DeleteView):
    model = video
    success_url = reverse_lazy('videos:index')



